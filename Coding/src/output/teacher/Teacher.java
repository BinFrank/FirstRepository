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
		 * super�������ڹ��캯����һ��
		 */
//		super();
	}

	public static void main(String[] args) {
		Teacher teacher = new Teacher();
		/*
		 * this��ʾ��ǰ��Ķ�����static���εķ���������ֱ�ӵ��ã�����Ҫ��������������static�ﲻ����this
		 */
//		System.out.println(this.name);
	}

}
