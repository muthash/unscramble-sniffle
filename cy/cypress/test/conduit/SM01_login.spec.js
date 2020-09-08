describe('Login', () => {
    it('Sign in', () => {
        cy.visit('/')
        cy.get('.navbar').contains('Sign in').click()
        cy.get('input[type=email]').type('muthash@github.com')
        cy.get('input[type=password]').type('muthash123')
        cy.get('.btn').contains('Sign in').should('be.visible').click()
    })
})