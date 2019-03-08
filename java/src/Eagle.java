public class Eagle implements Animal, Bird {

    @Override
    public void eat() {
        System.out.println("eat worm");
    }

    @Override
    public void move() {
        System.out.println("Move by flying");
    }

    @Override
    public void voice() {
        System.out.println("kwaaakkkk!!");
    }
}
