package output.hello;
/*
 * 输出序列：
 *  static A
	static B
	I'm A class
	HelloA
	I'm B class
	HelloB
 */
/*
 * 输出序列解析：
 * 首先加载类时会初始化static，所以首先输出 static A  static B；
 * 其次创建子类对象时，会先初始化父类，所以会调用父类中的构造函数，而大括号里的内容会在构造函数执行前执行。
 * 	所以是 I'm A class  HelloA 和 I'm B class  HelloB
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
