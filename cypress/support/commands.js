Cypress.Commands.add("SignIn", () => {
    cy.visit('https://react-redux.realworld.io/#/login')
    cy.title().should('eq', 'Conduit')
    cy.location('protocol').should('eq', 'https:')
    cy.get('form').within(($form) => {
        cy.get('input[type = "email"]').type('muthash@github.com')
        cy.get('input[type = "password"]').type('muthash123')
        cy.root().submit()
    })
    cy.contains('Your Feed', {timeout:10000}).should('be.visible')
    cy.contains('Global Feed').should('be.visible')
})