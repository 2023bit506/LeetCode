public class Problem_1929 {
    public static int[] result(int[] nums)
    {
        int[] arr = new int[nums.length*2];
        for(int i=0;i<nums.length;i++)
        {
            arr[i] = nums[i];
            arr[i + nums.length] = nums[i];
        }
        return arr;
    }
    public static void main(String[] args) {
        int[] nums = {1,2,3};
        int[] res11 = result(nums);

        for(int num:res11)
        {
            System.out.print(num + " ");
        }
    }
}
