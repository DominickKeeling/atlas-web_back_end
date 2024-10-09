-- create a trigger decreasing the number items in the items table after adding a new order
DELIMITER //

CREATE TRIGGER trigger_items_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  -- decreases the quantity
  UPDATE items
  SET quantity = quantity - NEW.number
  WHERE name = NEW.item_name;
END //

DELIMITER ;