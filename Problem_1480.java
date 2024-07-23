public class Problem_1480 {

    public static int[] runningSum(int[] nums) {

        int[] result = new int[nums.length];
        int sum = 0;

        for(int i=0;i<nums.length;i++)
        {
            sum += nums[i];
            result[i] = sum;
        }
        return result;
 
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5,6};
        int[] runningSumArry = runningSum(nums);

        for(int num:runningSumArry)
        {
            System.out.print(num + " ");
        }
    }
}
