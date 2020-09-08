describe('Create and mark-unmark as favorite', () => {
    
    Cypress.config('pageLoadTimeout', 100000)
    
    before("SignIn", () => {
        cy.SignIn()
    })

    it('Create a post', function(){
        cy.get('ul.navbar-nav').children().as('menu')
        cy.get('@menu').contains('New Post').click()
        cy.hash().should('include','#/editor')
        cy.get('form').within(($form) => {
            cy.get('input').first().type('Test')
            cy.get('input').eq(1).type('Test 1')
            cy.get('textarea').last().type('Test 2')
            cy.contains('Publish Article').click()
        })
        cy.url().should('include','article')
    })

    it('Mark-unmark as favorite', () => {
        cy.get('ul.navbar-nav').children().as('menu')
        cy.get('@menu').contains('muthash').click()
        cy.contains('My Articles').should('be.visible')
        cy.get('.ion-heart').first().click()
        cy.contains('Favorited Articles').click()
        cy.url().should('include', 'favorites')
        cy.get('.btn-primary').first().then(($fav) => {
            return $fav.text()  
        }).as('favCount')
        cy.get('@favCount').then($cnt => {
            expect(parseInt($cnt)).to.eq(1)
        })
        cy.get('.btn-primary').first().click()
        cy.reload()
        cy.contains('No articles are here... yet.').should('be.visible')
        cy.go('back')
    })
})