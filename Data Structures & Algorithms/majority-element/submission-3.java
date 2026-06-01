class Solution {
    public int majorityElement(int[] nums){
        int k = 1;
        int num = nums[0];
        for(int i = 1; i<nums.length; i++)
        {
            if(num != nums[i])
            {
                k--;
                if(k==0)
                {num = nums[i]; k = 1;}
            }
            else{
                k++;
            }
        }
        return num;
    }
}