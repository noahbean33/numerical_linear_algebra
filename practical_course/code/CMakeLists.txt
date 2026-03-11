cmake_minimum_required(VERSION 3.14)
project(practical_nla_examples LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# ── Find Eigen (header-only) ──────────────────────────────────────────
find_package(Eigen3 3.3 REQUIRED NO_MODULE)

# ── Optional: link Intel MKL for faster BLAS ──────────────────────────
# find_package(MKL QUIET)
# if(MKL_FOUND)
#     message(STATUS "Intel MKL found — linking for accelerated BLAS")
#     add_definitions(-DEIGEN_USE_MKL_ALL)
# endif()

# ── Executables ───────────────────────────────────────────────────────
add_executable(heat_rod_3x3       heat_rod_3x3.cpp)
add_executable(heat_rod_1M        heat_rod_1M.cpp)
add_executable(cache_locality     cache_locality.cpp)
add_executable(gemm_benchmark     gemm_benchmark.cpp)
add_executable(svd_solve          svd_solve.cpp)
add_executable(sparse_poisson_2d  sparse_poisson_2d.cpp)
add_executable(iterative_solve    iterative_solve.cpp)
add_executable(pitfalls_demo      pitfalls_demo.cpp)

# ── Link Eigen to all targets ─────────────────────────────────────────
set(ALL_TARGETS
    heat_rod_3x3
    heat_rod_1M
    cache_locality
    gemm_benchmark
    svd_solve
    sparse_poisson_2d
    iterative_solve
    pitfalls_demo
)

foreach(tgt ${ALL_TARGETS})
    target_link_libraries(${tgt} PRIVATE Eigen3::Eigen)
    # if(MKL_FOUND)
    #     target_link_libraries(${tgt} PRIVATE MKL::MKL)
    # endif()
endforeach()

# ── Compiler flags ────────────────────────────────────────────────────
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    add_compile_options(-O2 -march=native -Wall -Wextra)
elseif(MSVC)
    add_compile_options(/O2 /W3)
endif()
