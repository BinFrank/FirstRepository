package output.test1;

/*
 * ͬһ�ļ������ж���ֻ࣬����һ������public�����ļ����Ʊ����������һ��
 * 
 * ���ļ���û��public�࣬���ļ�����������ȡ
 * 
 * main�������Ǳ������public���в���ִ��
 * 
 * ��public��Ŀ������public���ڰ��ڰ�����ɷ���
 */
class Super {
	public Integer getLenght() {
		return new Integer(4);
	}
}

public class Sub extends Super {

	public Integer getLenght() {
		return new Integer(5);
	} 

	public static void main(String[] args) {
		Super sooper = new Super();
		Sub sub = new Sub();
		System.out.println(sooper.getLenght().toString() + "," + sub.getLenght().toString());
	}

}
