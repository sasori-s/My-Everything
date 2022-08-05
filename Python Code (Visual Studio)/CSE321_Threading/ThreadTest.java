class MyThread extends Thread{

    public MyThread(String name){
        super(name);
    }

    @Override
    public void run(){
        for ( int i = 0; i < 5; i++){
            System.out.println("This output is from " + getName() + ':' + i);
        try{
            sleep(1000);
        } catch (InterruptedException e){
            e.printStackTrace();
        }
    }
    }
}


public class ThreadTest {
   public static void main(String[] args) {
       MyThread myThread1 = new MyThread("My Thread 1");
       MyThread myThread2 = new MyThread("My Thread 2");
       MyThread myThread3 = new MyThread("My Thread 3");
       MyThread myThread4 = new MyThread("My Thread 4");
       
    //    System.out.println(myThread1.getState()); 

       myThread1.start();
       myThread2.start();
       myThread3.start();
       myThread4.start();

       try{
       myThread1.join();
       myThread2.join();
       myThread3.join();
       myThread4.join();

       } catch(InterruptedException e){
           e.printStackTrace();
       }

       if (!myThread2.isAlive()){
           System.out.println(myThread2.getName() + "is DEAD!!!");
       }

    //    System.out.println(myThread1.getState());
    System.out.println("All threads are done!!!!");
   } 
}
