// describe('Login', () => {
//     it('Sign in', () => {
//         cy.visit('/')
//         cy.get('.navbar').contains('Sign in').click()
//         cy.fixture('userLoginDetails').then((user) => {
//             cy.get('input[type=email]').type(user.email)
//             cy.get('input[type=password]').type(user.password)
//         })
//         cy.get('.btn').contains('Sign in').should('be.visible').click()
//     })
// })

// describe('Login', () => {
//     let userDetails;
//     beforeEach(() => {
//         cy.fixture('userLoginDetails').then((user) => {
//             userDetails = user
//         })
//     })

//     it('Sign in', () => {
//         cy.visit('/')
//         cy.get('.navbar').contains('Sign in').click()
//         cy.get('input[type=email]').type(userDetails.email)
//         cy.get('input[type=password]').type(userDetails.password)
//         cy.get('.btn').contains('Sign in').should('be.visible').click()
//     })
// })

describe('Login', function () {
    beforeEach(function () {
        cy.fixture('userLoginDetails').as('user')
    })
    it('Sign in', function () {
        cy.visit('/')
        cy.get('.navbar').contains('Sign in').click()
        cy.get('input[type=email]').type(this.user.email)
        cy.get('input[type=password]').type(this.user.password)
        cy.get('.btn').contains('Sign in').should('be.visible').click()
    })
})
