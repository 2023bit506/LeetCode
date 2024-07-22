// Check given number is palendrome or not

class Problem_9{

    static boolean isPalendrome(int x)
    {
        int temp = x;
        int rev = 0;

        while (x>0) {
            int digit = x % 10;
            rev = (rev*10)+digit;
            x = x /10;
        }

        if (rev == temp) {
            return  true;
        }
        else
        {
            return  false;
        }
    }
    public static void main(String[] args) {
        System.out.println(Problem_9.isPalendrome(787));
    }
}