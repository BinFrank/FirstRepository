package output.test1;

/*
 * 同一文件中若有多个类，只能有一个类是public，且文件名称必须与该类名一致
 * 
 * 若文件中没有public类，则文件名可以随意取
 * 
 * main方法不是必须放在public类中才能执行
 * 
 * 加public的目的在于public类在包内包外均可访问
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
