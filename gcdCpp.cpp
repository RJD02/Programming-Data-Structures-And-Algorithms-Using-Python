#include<iostream>
#include<chrono>
using namespace std;
typedef long long ll;
int gcd(long long m, long long n) {
  if(m < n) {
    long long temp = m;
    m = n;
    n = temp;
  }
  if(m % n  == 0)
    return n;
  return gcd(n, m % n);
}

int main() {
  std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
	start = std::chrono::high_resolution_clock::now();
  long long m, n;
  cin >> m >> n;
  cout << gcd(m, n);
	end = std::chrono::high_resolution_clock::now();
	ll elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(end-start).count();
	cout << "\nElapsed Time: " << elapsed_time << "ms\n";
  return 0;
}
