class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        """
        class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int len = flowerbed.length;
        int place = 0;
        int t = 1;
        for (int i = 0; i < len; i++) {
            if (flowerbed[i] == 0)
                t++;
            else {
                place += (t - 1) / 2;
                t = 0;
            }
        }
        place += t / 2;
        return n <= place;
    }
}
        """