package output.test3;

import java.util.ArrayList;
import java.util.List;

public class Test {

	public static void main(String[] args) {
//		String s = Integer.toBinaryString(161);
//		System.out.println(s);
//		
//		char[] temp = s.toCharArray();
//		int[] result = new int[temp.length];  
//        for(int i=0;i<temp.length;i++) {
//            result[i]=temp[i]-48;
//        }
//        
//        Integer count = 0;
//        List<Integer> list = new ArrayList<>();
//        
//        for(int i=0;i<result.length;i++){
//        	if(result[i] == 1){
//        		count += 1;
//        		list.add(i+1);
//        	}
//        }
//        list.add(0, count);
//        for(Integer index : list){
//        	System.out.println(index);
//        }
		
		
		String str1 = "¼ªÄ·Ï²»¶ÂíÈð";
		String str2 = "Ï²»¶ÎÒ";
		if(str1.indexOf(str2) != -1){
			System.out.println("°üº¬");
		}else{
			System.out.println("²»°üº¬");
		}
      
	}

}
