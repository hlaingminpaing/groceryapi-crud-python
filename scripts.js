$(document).ready(function () {
    var API_ENDPOINT = "https://8emw4c5w0b.execute-api.ap-southeast-1.amazonaws.com/uat/items";

    // Handle Save Grocery Data (Add Item)
    document.getElementById("addItem").onclick = function() {
        var inputData = {
            "itemid": $('#itemid').val(),
            "name": $('#name').val(),
            "category": $('#category').val(),
            "price": $('#price').val()
        };

        console.log("Input Data: ", inputData); // Log input data for debugging
        
        // Perform AJAX POST request to save grocery data
        $.ajax({
            url: API_ENDPOINT,
            type: 'POST',
            data: JSON.stringify(inputData),
            contentType: 'application/json; charset=utf-8',
            success: function(response) {
                console.log('Response:', response); // Log the response for debugging
                $('#grocerySaved').text("Grocery Item Saved!").show().fadeOut(3000);
                $('#itemid, #name, #category, #price').val(''); // Clear input fields
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('Error:', textStatus, errorThrown); // Log the error
                alert("Error saving grocery data.");
            }
        });
    };

    // Handle Get All Grocery Items Data (View All Items)
    document.getElementById("getItems").onclick = function() {
        $.ajax({
            url: API_ENDPOINT,
            type: 'GET',
            contentType: 'application/json; charset=utf-8',
            success: function(response) {
                if (Array.isArray(response.body)) {
                    $('#groceryTable tbody').empty(); // Clear existing rows
                    $('#showItems').show(); // Display the table after fetching data
                    response.body.forEach(function(data) {
                        $("#groceryTable tbody").append("<tr> \
                            <td>" + data['ItemID'] + "</td> \
                            <td>" + data['Name'] + "</td> \
                            <td>" + data['Category'] + "</td> \
                            <td>" + data['Price'] + "</td> \
                        </tr>");
                    });
                } else {
                    alert("Unexpected response format.");
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('Error:', textStatus, errorThrown); // Log the error
                alert("Error retrieving grocery data.");
            }
        });
    };

    // Handle Update Grocery Item
    document.getElementById("updateItem").onclick = function() {
        var inputData = {
            "itemid": $('#itemid').val(),
            "name": $('#name').val(),
            "category": $('#category').val(),
            "price": $('#price').val()
        };

        console.log("Input Data: ", inputData); // Log input data for debugging
        
        // Perform AJAX PUT request to update grocery data
        $.ajax({
            url: API_ENDPOINT + '/' + $('#itemid').val(), // Ensure the item ID is part of the URL
            type: 'PUT',
            data: JSON.stringify(inputData),
            contentType: 'application/json; charset=utf-8',
            success: function(response) {
                console.log('Response:', response); // Log the response for debugging
                $('#grocerySaved').text("Grocery Item Updated!").show().fadeOut(3000);
                $('#itemid, #name, #category, #price').val(''); // Clear input fields
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('Error:', textStatus, errorThrown); // Log the error
                alert("Error updating grocery data.");
            }
        });
    };

    // Handle Delete Grocery Item
    document.getElementById("deleteItem").onclick = function() {
        var itemId = $('#itemid').val();
        
        if (!itemId) {
            alert("Please enter the Item ID to delete.");
            return;
        }

        console.log("Deleting item with ID: ", itemId); // Log item ID for debugging
        
        // Perform AJAX DELETE request to delete grocery data
        $.ajax({
            url: API_ENDPOINT + '/' + itemId,
            type: 'DELETE',
            contentType: 'application/json; charset=utf-8',
            success: function(response) {
                console.log('Response:', response); // Log the response for debugging
                $('#grocerySaved').text("Grocery Item Deleted!").show().fadeOut(3000);
                $('#itemid, #name, #category, #price').val(''); // Clear input fields
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error('Error:', textStatus, errorThrown); // Log the error
                $('#grocerySaved').text("Error deleting grocery item.").show().fadeOut(3000); // Show error message
            }
        });
    };
});
