package output.test2;
/*
 * 创建子类对象时，会调用父类的构造方法
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
