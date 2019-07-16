package output.test;

public class Test {
	static int i = 0;
	public int aMethod(){
		/*
		 * static用于修饰成员变量和方法，在加载类时就以及初始化
		 * 而方法内的变量随着方法的使用而产生、方法的结束而回收
		 * 所以不允许在方法内创建修饰符(static,public,private等)修饰的变量
		 * 可用final，但使用final修饰的变量不可改变、修饰的方法不能重写
		 */
//		static int i = 0;
		i++;
		return i;
	}

	public static void main(String[] args) {
		Test test = new Test();
		test.aMethod();
		int j = test.aMethod();
		System.out.println(j);
	}

}
