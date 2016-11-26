#include <iostream>
#include <unordered_map>

using namespace std;

void solve(long long, long long);
int helper(long long, unordered_map<long long, int>&, bool, long long[]);

int main() {
   long long a;
   long long b;

   cin >> a;
   cin >> b;

   while (a != 0 && b != 0) {
      solve(a, b);

      cin >> a;
      cin >> b;
   }
}

void solve(long long a, long long b) {
   unordered_map<long long, int> counts(524);
   
   long long meeting_location[1] = {};
   counts[1] = 1;

   int a_count = helper(a, counts, false, meeting_location);
   int b_count = helper(b, counts, true, meeting_location);

   cout << a << " needs " << a_count - counts.find(meeting_location[0])->second << " steps, ";
   cout << b << " needs " << b_count - counts.find(meeting_location[0])->second << " steps, ";
   cout << "they meet at " << meeting_location[0] << endl;
}

int helper(long long num, unordered_map<long long, int>& counts, 
      bool check_counts, long long meet[]) {
   int current_count = 1;
   if (check_counts) {
      /* See if this number has already been recorded. */
      auto count = counts.find(num);
      if (count != counts.end()) {
         /* Record the number where they overlapped. */
         meet[0] = num;

         return current_count + count->second - 1;
      }
   }
   if (num > 1) {
      if (num % 2 == 0) {
         current_count += helper(num / 2, counts, check_counts, meet);
      } else {
         current_count += helper((3 * num) + 1, counts, check_counts, meet);
      }

      if (!check_counts) {
         /* Need to record the current count. */
         counts[num] = current_count;
      }
   }
   return current_count;
}
