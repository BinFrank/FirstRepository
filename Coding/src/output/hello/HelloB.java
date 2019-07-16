package output.hello;
/*
 * ������У�
 *  static A
	static B
	I'm A class
	HelloA
	I'm B class
	HelloB
 */
/*
 * ������н�����
 * ���ȼ�����ʱ���ʼ��static������������� static A  static B��
 * ��δ����������ʱ�����ȳ�ʼ�����࣬���Ի���ø����еĹ��캯������������������ݻ��ڹ��캯��ִ��ǰִ�С�
 * 	������ I'm A class  HelloA �� I'm B class  HelloB
 */
class HelloA{
	public HelloA(){
		System.out.println("HelloA");
	}
	{
		System.out.println("I'm A class");
	}
	static{
		System.out.println("static A");
	}
}

public class HelloB extends HelloA{
	public HelloB(){
		System.out.println("HelloB");
	}
	{
		System.out.println("I'm B class");
	}
	static{
		System.out.println("static B");
	}

	public static void main(String[] args) {
		new HelloB();
	}

}
