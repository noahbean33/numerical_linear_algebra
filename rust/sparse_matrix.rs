use std::fmt;

/// A sparse matrix represented in Compressed Sparse Row (CSR) format.
///
/// The matrix is stored as:
/// - `values`: nonzero values in row-major order.
/// - `col_indices`: corresponding column indices for each value.
/// - `row_offsets`: indices in `values` at which each row starts.
///   Length is `rows + 1`; the last element equals the total number of nonzeros.
#[derive(Debug, Clone)]
pub struct SparseMatrix {
    rows: usize,
    cols: usize,
    values: Vec<f64>,
    col_indices: Vec<usize>,
    row_offsets: Vec<usize>,
}

impl SparseMatrix {
    /// Constructs a new SparseMatrix given the raw CSR components.
    pub fn new(
        rows: usize,
        cols: usize,
        values: Vec<f64>,
        col_indices: Vec<usize>,
        row_offsets: Vec<usize>,
    ) -> Self {
        assert_eq!(
            row_offsets.len(),
            rows + 1,
            "row_offsets length must be rows + 1"
        );
        assert_eq!(
            values.len(),
            col_indices.len(),
            "values and col_indices must have the same length"
        );
        assert_eq!(
            *row_offsets.last().unwrap(),
            values.len(),
            "last row_offset must equal nnz"
        );
        SparseMatrix {
            rows,
            cols,
            values,
            col_indices,
            row_offsets,
        }
    }

    /// Constructs a SparseMatrix from a Coordinate (COO) representation.
    /// Each entry in `entries` is a tuple `(row_index, col_index, value)`.
    pub fn from_coo(rows: usize, cols: usize, mut entries: Vec<(usize, usize, f64)>) -> Self {
        // Sort the entries: first by row index, then by column index.
        entries.sort_by_key(|&(r, c, _)| (r, c));
        let nnz = entries.len();
        let mut row_offsets = vec![0usize; rows + 1];

        // Count nonzero elements per row.
        for &(r, _, _) in &entries {
            row_offsets[r + 1] += 1;
        }
        // Compute cumulative sum to convert counts into starting indices.
        for i in 1..=rows {
            row_offsets[i] += row_offsets[i - 1];
        }

        // Temporary copy to track insertion positions per row.
        let mut current_offset = row_offsets.clone();
        let mut values = vec![0.0; nnz];
        let mut col_indices = vec![0usize; nnz];

        // Insert each COO entry into the CSR arrays.
        for (r, c, v) in entries {
            let pos = current_offset[r];
            values[pos] = v;
            col_indices[pos] = c;
            current_offset[r] += 1;
        }

        SparseMatrix {
            rows,
            cols,
            values,
            col_indices,
            row_offsets,
        }
    }

    /// Returns the number of rows.
    pub fn nrows(&self) -> usize {
        self.rows
    }

    /// Returns the number of columns.
    pub fn ncols(&self) -> usize {
        self.cols
    }

    /// Returns the number of stored nonzero entries.
    pub fn nnz(&self) -> usize {
        self.values.len()
    }

    /// Retrieves the value at position (i, j).  Returns 0.0 if the
    /// entry is not stored.
    pub fn get(&self, i: usize, j: usize) -> f64 {
        let start = self.row_offsets[i];
        let end = self.row_offsets[i + 1];
        for idx in start..end {
            if self.col_indices[idx] == j {
                return self.values[idx];
            }
        }
        0.0
    }

    /// Multiplies the sparse matrix by a dense vector `x` and returns
    /// the result vector y = A * x.
    pub fn mul_dense(&self, x: &[f64]) -> Vec<f64> {
        assert_eq!(
            x.len(),
            self.cols,
            "Dimension mismatch: vector length must equal number of matrix columns."
        );
        let mut result = vec![0.0; self.rows];
        for row in 0..self.rows {
            let start = self.row_offsets[row];
            let end = self.row_offsets[row + 1];
            for idx in start..end {
                result[row] += self.values[idx] * x[self.col_indices[idx]];
            }
        }
        result
    }

    /// Returns the transpose of this matrix as a new SparseMatrix in
    /// CSR format (which is equivalent to CSC of the original).
    pub fn transpose(&self) -> SparseMatrix {
        let t_rows = self.cols;
        let t_cols = self.rows;
        let nnz = self.nnz();

        // Count nonzeros per column of A (= per row of A^T).
        let mut row_offsets = vec![0usize; t_rows + 1];
        for &c in &self.col_indices {
            row_offsets[c + 1] += 1;
        }
        for i in 1..=t_rows {
            row_offsets[i] += row_offsets[i - 1];
        }

        let mut values = vec![0.0; nnz];
        let mut col_indices = vec![0usize; nnz];
        let mut current_offset = row_offsets.clone();

        for row in 0..self.rows {
            let start = self.row_offsets[row];
            let end = self.row_offsets[row + 1];
            for idx in start..end {
                let c = self.col_indices[idx];
                let pos = current_offset[c];
                values[pos] = self.values[idx];
                col_indices[pos] = row; // original row becomes column in A^T
                current_offset[c] += 1;
            }
        }

        SparseMatrix {
            rows: t_rows,
            cols: t_cols,
            values,
            col_indices,
            row_offsets,
        }
    }

    /// Adds two sparse matrices of the same dimensions and returns the
    /// result as a new SparseMatrix.  Uses a merge-style traversal of
    /// each row.
    pub fn add(&self, other: &SparseMatrix) -> SparseMatrix {
        assert_eq!(self.rows, other.rows, "Row dimension mismatch");
        assert_eq!(self.cols, other.cols, "Column dimension mismatch");

        let mut values = Vec::new();
        let mut col_indices = Vec::new();
        let mut row_offsets = vec![0usize; self.rows + 1];

        for row in 0..self.rows {
            let a_start = self.row_offsets[row];
            let a_end = self.row_offsets[row + 1];
            let b_start = other.row_offsets[row];
            let b_end = other.row_offsets[row + 1];

            let mut ai = a_start;
            let mut bi = b_start;

            // Merge the two sorted column-index streams for this row.
            while ai < a_end && bi < b_end {
                let ca = self.col_indices[ai];
                let cb = other.col_indices[bi];
                if ca < cb {
                    values.push(self.values[ai]);
                    col_indices.push(ca);
                    ai += 1;
                } else if ca > cb {
                    values.push(other.values[bi]);
                    col_indices.push(cb);
                    bi += 1;
                } else {
                    // Same column — sum the values.
                    let s = self.values[ai] + other.values[bi];
                    if s != 0.0 {
                        values.push(s);
                        col_indices.push(ca);
                    }
                    ai += 1;
                    bi += 1;
                }
            }
            // Drain remaining entries from A.
            while ai < a_end {
                values.push(self.values[ai]);
                col_indices.push(self.col_indices[ai]);
                ai += 1;
            }
            // Drain remaining entries from B.
            while bi < b_end {
                values.push(other.values[bi]);
                col_indices.push(other.col_indices[bi]);
                bi += 1;
            }

            row_offsets[row + 1] = values.len();
        }

        SparseMatrix {
            rows: self.rows,
            cols: self.cols,
            values,
            col_indices,
            row_offsets,
        }
    }

    /// Converts the sparse matrix to a dense 2D vector (row-major).
    pub fn to_dense(&self) -> Vec<Vec<f64>> {
        let mut dense = vec![vec![0.0; self.cols]; self.rows];
        for row in 0..self.rows {
            let start = self.row_offsets[row];
            let end = self.row_offsets[row + 1];
            for idx in start..end {
                dense[row][self.col_indices[idx]] = self.values[idx];
            }
        }
        dense
    }
}

/// Implements a simple display for the sparse matrix to visualize
/// its CSR structure.
impl fmt::Display for SparseMatrix {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        writeln!(
            f,
            "SparseMatrix ({}×{}, {} nonzeros) in CSR format:",
            self.rows,
            self.cols,
            self.nnz()
        )?;
        writeln!(f, "  row_offsets:  {:?}", self.row_offsets)?;
        writeln!(f, "  col_indices:  {:?}", self.col_indices)?;
        writeln!(f, "  values:       {:?}", self.values)?;
        Ok(())
    }
}

// ---------------------------------------------------------------------------
// Main — demonstrates construction, display, SpMV, transpose, and addition.
// ---------------------------------------------------------------------------

fn main() {
    // ------------------------------------------------------------------
    // 1. Build a 4×4 sparse matrix from COO triplets
    // ------------------------------------------------------------------
    let coo_entries = vec![
        (0, 1, 3.0),
        (0, 3, 4.5),
        (1, 0, 2.1),
        (2, 2, 5.0),
        (3, 1, 6.2),
        (3, 3, 7.7),
    ];

    let a = SparseMatrix::from_coo(4, 4, coo_entries);
    println!("{}", a);

    // ------------------------------------------------------------------
    // 2. Sparse matrix–vector multiplication  y = A * x
    // ------------------------------------------------------------------
    let x = vec![1.0, 2.0, 3.0, 4.0];
    let y = a.mul_dense(&x);
    println!("x        = {:?}", x);
    println!("y = A*x  = {:?}", y);
    println!();

    // ------------------------------------------------------------------
    // 3. Transpose
    // ------------------------------------------------------------------
    let at = a.transpose();
    println!("A^T:");
    println!("{}", at);

    // ------------------------------------------------------------------
    // 4. Sparse matrix addition  C = A + A^T
    // ------------------------------------------------------------------
    let c = a.add(&at);
    println!("C = A + A^T:");
    println!("{}", c);

    // ------------------------------------------------------------------
    // 5. Dense view of C for visual confirmation
    // ------------------------------------------------------------------
    println!("Dense view of C:");
    for row in c.to_dense() {
        println!("  {:?}", row);
    }
}
