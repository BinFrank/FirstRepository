package output.teacher;


class Person{
	public Person(){
		System.out.println("This is a Person");
	}
}

public class Teacher extends Person{
	private String name = "Tom";
	
	public Teacher(){
		System.out.println("This is a Teacher");
		/*
		 * super必须用在构造函数第一行
		 */
//		super();
	}

	public static void main(String[] args) {
		Teacher teacher = new Teacher();
		/*
		 * this表示当前类的对象，由static修饰的方法是由类直接调用，不需要创建对象，所以在static里不能用this
		 */
//		System.out.println(this.name);
	}

}
