package output.test2;
/*
 * �����������ʱ������ø���Ĺ��췽��
 */
class Base{
	Base(){
		System.out.print("Base");
	}
}

public class Alpha extends Base{

	public static void main(String[] args) {
		new Alpha();
		new Base();
	}

}
