// We use this preprocessor directive to cause the current source file to be included only once
// in a single compilation.
#pragma once
#include "common/experimental/weimingliu/codelab/cpp/josephus.pb.h"

int SolveJosephusProblem(int n, int k);

// Please implement this function add unit test for it
const ::interface::experimental::weimingliu::Person SolveJosephusProblem(
    interface::experimental::weimingliu::JosephusProblem);
