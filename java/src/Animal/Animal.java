package Animal;

public class Animal {
    private String name;
    private double averageWeight;
    private int numberOfLegs;

    public String getName() {
        return name;
    }

    public double getAverageWeight() {
        return averageWeight;
    }

    public int getNumberOfLegs() {
        return numberOfLegs;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAverageWeight(double averageWeight) {
        this.averageWeight = averageWeight;
    }

    public void setNumberOfLegs(int numberOfLegs) {

        this.numberOfLegs = numberOfLegs;
    }

    public void eat() {
        System.out.println("This animal eats insects.");
    }

    public static class AnimalBuilder {

        private String name;
        private double averageWeight;
        private int numberOfLegs;

        public AnimalBuilder() {
        }

        public AnimalBuilder setName(String name) {
            this.name = name;
            return this;
        }

        public AnimalBuilder setAverageWeight(double averageWeight) {
            this.averageWeight = averageWeight;
            return this;
        }

        public AnimalBuilder setNumberOfLegs(int numberOfLegs) {
            this.numberOfLegs = numberOfLegs;
            return this;
        }

        public Animal build(){
            Animal a = new Animal();
            a.averageWeight = this.averageWeight;
            a.name = this.name;
            a.numberOfLegs = this.numberOfLegs;
            return a;
        }
    }
}