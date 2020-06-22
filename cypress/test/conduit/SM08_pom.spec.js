import Login from '../pageObjects/login'

describe('Login', () => {
    const login = new Login()
    
    it('Sign in', () => {
        cy.visit('/')
        cy.get('.navbar').contains('Sign in').click()
        login.email().type('muthash@github.com')
        login.password().type('muthash123')
        login.signInButton().should('be.visible').click()
    })
})