class Fish implements Animal{

    @Override
    public void eat() {
        System.out.println("Eat seafood");
    }

    @Override
    public void move() {
        System.out.println("Moves by swimming.");
    }
}