#gold 1
#c++
#같은 로직의 python코드는 통과를 못함

'''
#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;
using lint = long long;

unordered_map<lint, int> cnt;
int N;
string s;

inline int ctoi(char c) {
	if ('a' <= c && c <= 'z') return c - 'a';
	return c - 'A' + 26;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	cin >> N >> s;

	lint status = 0, ans = 0;
	cnt[status]++;
	for (int i = 0; i < N; i++) {
		int b = ctoi(s[i]);
		status ^= (1LL << b);
		ans += cnt[status];  //모두 짝수인 경우
		for (int j = 0; j < 52; j++) {  //한놈만 홀수인 경우
			lint newstat = status ^ (1LL << j);
			if (cnt.find(newstat) != cnt.end()) ans += cnt[newstat];
		}
		cnt[status]++;
	}
	cout << ans;

	return 0;
}
'''