import Animal.Animal;

public class Main {

    public static void main(String[] args) {
        Animal myAnimal = new Animal.AnimalBuilder()
                .setName("First Animal")
                .setAverageWeight(15.5)
                .setNumberOfLegs(2)
                .build();


        System.out.println(myAnimal.getName());


        Animal myAnimal2 = new Animal.AnimalBuilder()
                .build();

        System.out.println(myAnimal2.getName());

    }
}
