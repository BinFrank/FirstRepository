package output.test;

public class Test {
	static int i = 0;
	public int aMethod(){
		/*
		 * static�������γ�Ա�����ͷ������ڼ�����ʱ���Լ���ʼ��
		 * �������ڵı������ŷ�����ʹ�ö������������Ľ���������
		 * ���Բ������ڷ����ڴ������η�(static,public,private��)���εı���
		 * ����final����ʹ��final���εı������ɸı䡢���εķ���������д
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
