#include <iostream>
#include <set>
using namespace std;

int main() {
   long long ribbon_size;
   cin >> ribbon_size;

   set<long long> lengths;
   long long input;
   while (cin >> input)
      lengths.insert(input);

   long long min = *lengths.begin();
   long long dp[4005] = {};
   for (int i = min; i <= ribbon_size; i++) {
      for (auto piece : lengths) {
         /* Idea here:
          * We want to get to length i using the MOST number of ribbon slices
          * possible.
          */
         /* First check if we're in-bounds.
          * If we are in-bounds, recall: we can add 1 piece to another piece
          * to get to i. But note that there will be a LOT of ribbon lengths that we
          * CANNOT get to because they are not a multiple of any piece.
          * Those will be dp[i - piece] = 0 where i - piece > 0.
          */
         if (i - piece == 0 || (i - piece > 0 && dp[i - piece] != 0)) {
            /* If we're in-bounds, see how many pieces we use to get to length i. */
            long long new_pieces = dp[i - piece] + 1;
//             cout << "We can get to dp[" << i << "] using " << new_pieces << " piece(s) from dp[" << i - piece << "]"
//                << " by adding piece of length " << piece << endl;
            if (new_pieces > dp[i]) {
               dp[i] = new_pieces;
            }
         }
      }
   }
   cout << dp[ribbon_size] << endl;
}
