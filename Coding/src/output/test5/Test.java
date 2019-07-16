package output.test5;

/*
 * 判断字符串中是否有重复的元素
 */
public class Test {

	public static void main(String[] args) {
		String str = "abscde";
		Test t = new Test();
		if(t.IsRepeat(str)){
			System.out.println("有重复字符！");
		}else{
			System.out.println("没有重复字符！");
		}
	}

	public boolean IsRepeat(String str){
		char[] ch = str.toCharArray();
		for(int i=0; i<ch.length; i++){
			for(int j = i+1; j<ch.length; j++){
				if(ch[i] == ch[j]){
					return true;
				}
			}
		}
		return false;
		
	}

}
