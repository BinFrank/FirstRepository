package output.test4;
/*
 * ÄæĞòÊä³ö×Ö·û´®
 */
public class Test {

	public static void main(String[] args) {
		String str = "abcde";
		Test t = new Test();
		str = t.inversString(str);
		System.out.println(str);
	}
	
	public String inversString(String str){
		char[] ch = str.toCharArray();
		char[] ch2 = new char[ch.length];
		for(int i = 0; i < ch.length; i++){
			ch2[i] = ch[(ch.length - 1) - i];
		}
		String resultStr = String.valueOf(ch2);
		return resultStr;
	}

}
