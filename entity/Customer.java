public class Customer {
    private String name;
    private List<Order> orders;
                
    public void setName(String name) {
        this.name = name; 
    }

    public String getName() {
        return name; 
    }
                
    public void setOrders(List<Order> orders) {
        this.orders = orders; 
    }

    public List<Order> getOrders() {
        return orders; 
    }
}