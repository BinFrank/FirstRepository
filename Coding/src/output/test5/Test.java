package output.test5;

/*
 * �ж��ַ������Ƿ����ظ���Ԫ��
 */
public class Test {

	public static void main(String[] args) {
		String str = "abscde";
		Test t = new Test();
		if(t.IsRepeat(str)){
			System.out.println("���ظ��ַ���");
		}else{
			System.out.println("û���ظ��ַ���");
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
