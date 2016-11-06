#include <iostream>
#include <list>
#include <cmath>
using namespace std;

struct point {
   long long x;
   long long y;
};

int main() {
   point gun;
   int num_enemies;
   cin >> num_enemies;
   cin >> gun.x;
   cin >> gun.y;
//    cout << "There are " << num_enemies << " enemies." << endl;
//    cout << "Gun is at coord (" << gun.x << "," << gun.y << ")" << endl;
   list<point> enemies;
   for (int i = 0; i < num_enemies; i++) {
      point enemy;
      cin >> enemy.x;
      cin >> enemy.y;
      enemies.push_back(enemy);
   }

   int shots = 0;
   while (!enemies.empty()) {
      point e1 = enemies.front();

      for (auto it = ++enemies.begin(); it != enemies.end();) {
         point e2 = *it;

         /*
          * if enemy2 is collinear with enemy1 and gun,
          * it = enemies.erase(it)
          * else increment it
          */
         /* NOT absolute value because gun only shoots one direction (duh) */
         if ((e1.x-gun.x)*(e2.y-gun.y) == (e2.x-gun.x)*(e1.y-gun.y)) {
//             cout << "erased collinear point" << endl;
            it = enemies.erase(it);
         } else {
//             cout << "not collinear" << endl;
            ++it;
         }
      }

      enemies.pop_front();
      shots++;
   }
   cout << shots << endl;
}
