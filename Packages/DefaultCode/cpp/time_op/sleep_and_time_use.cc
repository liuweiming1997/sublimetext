#include <bits/stdc++.h>
#include "curl/curl.h"
#include "time.h"
#include <unistd.h>
#include "chrono"

using namespace std;

#define inf (0x3f3f3f3f)
typedef long long int LL;

void work() {
  std::chrono::time_point<std::chrono::system_clock> begin_time = std::chrono::system_clock::now();
  std::this_thread::sleep_for(std::chrono::milliseconds{5000});

  const double time_used = double(std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::system_clock::now() - begin_time).count());

  printf("%f\n", time_used);
}

int main(int argc, char *argv[]) {
  // freopen("data.txt", "r", stdin);
  work();
  return 0;
}
