public class Human implements Animal {
    @Override
    public void eat() {
        System.out.println("eat everything");
    }

    @Override
    public void move() {
        System.out.println("Moves by walking.");
    }
}
