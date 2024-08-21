public class LeetCode1512
{
    public static int numIdenticalPairs(int[] nums) {
        int temp = 0;
        for(int i=0;i<nums.length;i++)
        {
            for(int j=1;j<nums.length;j++)
            {
                if(nums[i] == nums[j] && i<j)
                {
                    temp += 1;
                }
            }
        }
        return temp;
    }
    public static void main(String[] args)
    {
        int[] nums = {1,2,1};
        int res =  numIdenticalPairs(nums);
        System.out.println(res);

    }
}