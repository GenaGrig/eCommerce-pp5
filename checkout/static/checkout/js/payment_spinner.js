function processPayment() {
    // Show the modal
    document.getElementById("paymentModal").style.display = "flex";

    // Show the spinner
    document.getElementById("paymentSpinner").style.display = "block";

    // Simulate payment processing (replace this with your actual payment processing logic)
    setTimeout(function () {
        // Hide the spinner after a simulated delay (replace this with your actual payment processing logic)
        document.getElementById("paymentSpinner").style.display = "none";

        // Hide the modal after processing is complete
        document.getElementById("paymentModal").style.display = "none";

        // Add any additional logic for the completion of the payment, e.g., redirect to a success page
        // window.location.href = "{% url 'payment_success' %}";

        // For now, let's simulate a redirect after a delay
        setTimeout(function () {
            window.location.href = "{% url 'checkout_success' %}";
        }, 10000); // 4 seconds delay
    }, 10000); // 4 seconds delay (replace this with your actual payment processing logic)
}

