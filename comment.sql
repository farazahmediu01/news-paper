CREATE TABLE "articles_comment" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "comment" varchar(255) NOT NULL,
    "article_id" bigint NOT NULL REFERENCES "articles_article" ("id") DEFERRABLE INITIALLY DEFERRED,
    "author_id" bigint NOT NULL REFERENCES "accounts_customuser" ("id") DEFERRABLE INITIALLY DEFERRED);

    
CREATE INDEX "articles_comment_article_id_59ff1409" ON "articles_comment" ("article_id");
CREATE INDEX "articles_comment_author_id_0524a063" ON "articles_comment" ("author_id");
COMMIT;