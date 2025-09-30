# This is a Feature file


Feature: Fill the Contact Form

    @formdata
    Scenario: Contact form page

        Given Create the class objects in cfp
        When Click Contact Form
        Then verify form page
        And Enter the data in form

#con 'behave' corren todas las pruebas
#con 'behave -t @formdata' solo corren los del tag
#para ejecutar solo un feature 'behave -t "@formdata" contactForm.feature'
#para ejecutar mas el reporte allure 'behave -t "@formdata" contactForm.feature -f allure_behave.formatter:AllureFormatter -o Allure_report'
#para poder ver el reporte ' allure serve C:\Users\Display\PycharmProjects\SeleniumBDDFW\Allure_report'
