#include <iostream>
using namespace std;

int main()
{
	uint32_t val = 2718281828;
	uint32_t max = 4294967295;
	int ans;
	long long solve;
	solve = max - val;
	solve = solve + 43;
	ans = solve + val;
	
	cout<< "Solve: " << solve << endl;
	cout<< "Out: " << ans << endl;
	
	return 0;
}
