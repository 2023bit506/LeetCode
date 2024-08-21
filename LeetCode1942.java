import java.util.ArrayList;
import java.util.List;

public class LeetCode1942
{
    public static List<Integer> findWordsContaining(String[] words, char x) {
        ArrayList<Integer> temp = new ArrayList<>();
        for(int i=0;i<words.length;i++)
        {
            if(words[i].contains(String.valueOf(x)))
            {
                temp.add(i);
            }
        }
        return temp;
    }
    public static void main(String[] args) {
        String[] words = {"Leet","Code"};
        char x = 'e';
        List<Integer> res = findWordsContaining(words,x);
        for(int num:res)
        {
            System.out.println(num);
        }

    }
}


//Second Approach

/*public static String[] findWordsContaining(String[] words, char x) {
    // ArrayList<Integer> temp = new ArrayList<>();
    for(int i=0;i<words.length;i++)
    {
        if(words[i].contains(String.valueOf(x)))
        {
            words[i] = String.valueOf(i);
        }
    }
    return words;
}
public static void main(String[] args) {
    String[] words = {"Leet","Code"};
    char x = 'e';
    String[] res = findWordsContaining(words,x);
    // List<Integer> res = findWordsContaining(words,x);
    // for(int num:res)
    // {
    //     System.out.print(num+" ");
    // }
    for(String num:res)
    {
        System.out.println(num);
    }

}*/