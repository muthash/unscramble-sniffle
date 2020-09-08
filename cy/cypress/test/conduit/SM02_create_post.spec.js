import { xorBy, eq } from "cypress/types/lodash";

describe("Create and mark-unmark as favorite", () => {
  it("Sign in", () => {
    cy.visit("/#/login");
    cy.title().should("eq", "Conduit");
    cy.location("protocol").should("eq", "https:");
    // cy.get('input[type=email]').type('muthash@github.com')
    // cy.get('input[type=password]').type('muthash123')
    // cy.get('.btn').contains('Sign in').should('be.visible').click()
    cy.get("form").within(($form) => {
      // cy.get() will only search for elements within form, not within the entire document
      cy.get('input[type = "email"]').type("muthash@github.com");
      cy.get('input[type = "password"]').type("muthash123");
      cy.root().submit(); // submits the form yielded from 'within'
    });
    cy.contains("Your Feed", { timeout: 10000 }).should("be.visible");
    cy.contains("Global Feed").should("be.visible");
  });

  it("Create a post", function () {
    // cy.contains('New Post').click()
    cy.get("ul.navbar-nav").children().contains("New Post").click();
    // cy.location('hash').should('include','#/editor')
    cy.hash().should("include", "#/editor");
    // cy.get('input[placeholder="Article Title"]').type('Test This Title')
    // cy.get('input[placeholder="What\'s this article about?"]').type('Test this input')
    // cy.get('textarea[placeholder="Write your article (in markdown)"]').type('Test this textarea')
    // cy.contains('Publish Article').click()
    cy.get("form").within(($form) => {
      cy.get("input").first().type("Test");
      cy.get("input").eq(1).type("Test 1");
      cy.get("textarea").last().type("Test 2");
      cy.contains("Publish Article").click();
    });
    cy.url().should("include", "article");
  });

  it("Mark-unmark as favorite", () => {
    // cy.get('.nav-link').contains('muthash').click()
    cy.get("ul.navbar-nav").children().contains("muthash").click();
    cy.contains("My Articles").should("be.visible");
    cy.get(".ion-heart").first().click();
    cy.contains("Favorited Articles").click();
    cy.url().should("include", "favorites");
    cy.get(".ion-heart").first().click();
    cy.reload();
    cy.contains("No articles are here... yet.").should("be.visible");
    cy.go("back");
    //cy.go(-1)
    //cy.go('forward')
    //cy.go(1)
  });
});
