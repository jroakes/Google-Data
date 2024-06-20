# Key Attributes


## GoogleApi.ContentWarehouse.V1.Model.GDocumentBaseContent

### ContentLength:
 - Description: The actual length of the content. If Representation is compressed, this equals to Content.UncompressedLength; otherwise, it is the length of the representation string.
 - Importance: Knowing the content length helps in understanding the size of the document, which can impact crawl efficiency and storage requirements.
 - Example: ContentLength: 2048

### ContentType:
 - Description: See enum ContentType in //depot/google3/webutil/http/content-type.proto.
 - Importance: The content type helps in identifying the nature of the document (e.g., text/html, application/json), which can influence how the content is processed and rendered.
 - Example: ContentType: 1 (assuming 1 corresponds to text/html)

### CrawlTime:
 - Description: Seconds since Unix epoch.
 - Importance: Crawl time indicates when the document was last crawled, which is crucial for understanding the freshness and relevance of the content.
 - Example: CrawlTime: "1633036800" (corresponding to a specific date and time)

### Language:
 - Description: A Language enum value. Default is English.
 - Importance: Language information is essential for correctly processing and indexing the content, as well as for serving the content to the appropriate audience.
 - Example: Language: 0 (assuming 0 corresponds to English)

### OriginalEncoding:
 - Description: If OriginalEncoding is present, the body part of the Representation was converted to UTF-8, Encoding was set to UTF8, and OriginalEncoding was set to the original encoding before conversion.
 - Importance: Knowing the original encoding helps in accurately rendering the content and preserving its integrity.
 - Example: OriginalEncoding: 5 (assuming 5 corresponds to ISO-8859-1)

### Representation:
 - Description: Possibly compressed for old documents. It is not compressed for docjoins produced by Raffia after ~2012.
 - Importance: The representation of the document is crucial for understanding how the content is stored and retrieved, impacting both storage efficiency and retrieval speed.
 - Example: Representation: "compressed_content_string"

### UncompressedLength:
 - Description: Historically present if Representation is compressed.
 - Importance: Knowing the uncompressed length is important for understanding the actual size of the content, which can affect processing and storage.
 - Example: UncompressedLength: 4096

### VisualType:
 - Description: Whether the content was visual right-to-left, and if so, what type of visual document it is. Default is NOT_VISUAL_DOCUMENT.
 - Importance: Visual type information is important for correctly rendering the content, especially for languages that are read right-to-left.
 - Example: VisualType: 2 (assuming 2 corresponds to a specific visual document type)

### crawledFileSize:
 - Description: Crawled file size of the original document.
 - Importance: Knowing the crawled file size helps in understanding the storage requirements and can impact crawl budget considerations.
 - Example: crawledFileSize: 10240

### encodedGeometryAnnotations:
 - Description: GeometryAnnotations, encoded with GeometryUtil::DeltaEncode() to reduce disk space usage.
 - Importance: Encoded geometry annotations are important for efficiently storing and retrieving spatial information related to the document.
 - Example: encodedGeometryAnnotations: "encoded_string"




## GoogleApi.ContentWarehouse.V1.Model.TrawlerFetchReplyDataRedirects

### BadSSLCertificate:
 - Description: The server SSL certificate chain in SSLCertificateInfo protobuf format.
 - Importance: Ensures the security and authenticity of the server, which can affect the trustworthiness and ranking of the site.
 - Example: "BadSSLCertificate": "MIIDdzCCAl+gAwIBAgIEU..."

### CrawlTimes:
 - Description: Per redirect hop timestamps.
 - Importance: Helps in understanding the timing and sequence of redirects, which can be useful for optimizing crawl efficiency and diagnosing issues.
 - Example: "CrawlTimes": {"initialHop": "2023-10-01T12:00:00Z", "redirectHop1": "2023-10-01T12:00:05Z"}

### DownloadTime:
 - Description: Download time of this fetch (ms).
 - Importance: Indicates the speed of the server response, which is a critical factor for user experience and SEO ranking.
 - Example: "DownloadTime": 150

### HSTSInfo:
 - Description: Specifies if the URL in a redirect was rewritten to HTTPS because of an HSTS policy for the domain.
 - Importance: Ensures that the site is served over a secure connection, which is important for security and SEO.
 - Example: "HSTSInfo": "HSTS_STATUS_REWRITTEN"

### HTTPResponseCode:
 - Description: The HTTP response code for this hop.
 - Importance: Helps in understanding the type of redirect and diagnosing issues with the redirect chain.
 - Example: "HTTPResponseCode": 302

### HopPageNoIndexInfo:
 - Description: Extra trawler::PageNoIndexInfo for this hop.
 - Importance: Indicates whether a page should be indexed or not, which is crucial for controlling which pages appear in search results.
 - Example: "HopPageNoIndexInfo": 1

### HopReuseInfo:
 - Description: trawler::ReuseInfo with status of IMS/IMF/cache query, for this hop.
 - Importance: Provides information on cache usage, which can affect crawl efficiency and server load.
 - Example: "HopReuseInfo": "CACHE_HIT"

### HopRobotsInfo:
 - Description: Extra trawler::RobotsInfo for this hop.
 - Importance: Indicates the robots.txt directives that apply to this hop, which is important for controlling crawler behavior.
 - Example: "HopRobotsInfo": 2

### HostId:
 - Description: If known, the hostid for this hop.
 - Importance: Identifies the specific host, which can be useful for diagnosing issues with specific servers or hosts.
 - Example: "HostId": "host123"

### HttpRequestHeaders:
 - Description: The HTTP headers sent for fetching this redirect hop.
 - Importance: Provides context on the request, which can be useful for debugging and optimizing server responses.
 - Example: "HttpRequestHeaders": "User-Agent: Googlebot"

### HttpResponseHeaders:
 - Description: The HTTP headers received from this redirect hop.
 - Importance: Provides context on the response, which can be useful for debugging and optimizing server responses.
 - Example: "HttpResponseHeaders": "Content-Type: text/html"

### RawTargetUrl:
 - Description: The raw URL of the redirect target, which may contain fragments or be non-canonicalized.
 - Importance: Helps in understanding the exact URL that was redirected to, which can be useful for debugging and ensuring correct URL handling.
 - Example: "RawTargetUrl": "[http://example.com/page#section](http://example.com/page#section)"

### RefreshTime:
 - Description: Refresh time in meta redirect tag.
 - Importance: Indicates the delay before a meta refresh redirect occurs, which can affect user experience and crawler behavior.
 - Example: "RefreshTime": 5

### RobotsTxt:
 - Description: The robots.txt used for this fetch.
 - Importance: Controls crawler access to the site, which is crucial for SEO and managing server load.
 - Example: "RobotsTxt": "User-agent: *\nDisallow: /private"

### SourceBody:
 - Description: For meta-redirects, this field may contain the body of the source document.
 - Importance: Provides the content of the source document, which can be useful for understanding the context of the redirect.
 - Example: "SourceBody": "<html>...</html>"

### TargetUrl:
 - Description: The canonicalized URL of the redirect target.
 - Importance: Ensures that the correct, canonical URL is followed, which is important for SEO and avoiding duplicate content issues.
 - Example: "TargetUrl": "[https://example.com/page](https://example.com/page)"

### Type:
 - Description: URL and redirect type.
 - Importance: Identifies the type of redirect, which can be useful for understanding and optimizing redirect behavior.
 - Example: "Type": "REDIRECT_TEMPORARILY"

## GoogleApi.ContentWarehouse.V1.Model.IndexingEmbeddedContentLinkInfo

### contentLength:
 - Description: Size of the HTTP body (payload of the HTTP response, excluding headers), pre-decompression. Equal to the value of the Content-Length header if any.
 - Importance: Knowing the content length helps in understanding the size of the resource being indexed, which can impact crawl efficiency and storage requirements.
 - Example: contentLength: 2048

### crawlDuration:
 - Description: Time spent downloading this resource, in milliseconds.
 - Importance: Crawl duration is crucial for optimizing the crawl budget and ensuring that resources are fetched efficiently.
 - Example: crawlDuration: 150

### crawlStatus:
 - Description: Enum values for crawl_status are defined in indexing/converter/proto/converter.proto.
 - Importance: The crawl status indicates the success or failure of the crawl, which is essential for diagnosing issues with resource fetching.
 - Example: crawlStatus: 1

### fetchStatus:
 - Description: Fetch status from trawler.
 - Importance: Fetch status provides detailed information about the result of the fetch operation, which is important for understanding the health and accessibility of the resource.
 - Example: fetchStatus: {status: "SUCCESS"}

### httpResponseLength:
 - Description: Size of the full HTTP response (headers and body pre-decompression). Semantically equal to content_length plus size of the HTTP headers.
 - Importance: The total response length helps in assessing the overall size of the resource, which can impact bandwidth usage and storage.
 - Example: httpResponseLength: 2200

### uncompressedContentLength:
 - Description: Size of the HTTP body (payload of the HTTP response, excluding headers), post-decompression. Equal to content_length if the body was not compressed to begin with.
 - Importance: Knowing the uncompressed content length is important for understanding the actual size of the resource after any compression has been removed, which can affect rendering and processing.
 - Example: uncompressedContentLength: 2048

### url:
 - Description: The URL of the embedded content.
 - Importance: The URL is a fundamental parameter for identifying and accessing the resource.
 - Example: url: "[https://example.com/resource](https://example.com/resource)"

### isCacheable:
 - Description: Indicates whether the resource is cacheable.
 - Importance: Cacheability affects how often a resource needs to be fetched, impacting crawl efficiency and server load.
 - Example: isCacheable: true

### fetchUrlResponseMetadata:
 - Description: Populated from embedded-content fetch server.
 - Importance: This metadata provides additional context about the fetch operation, which can be useful for debugging and optimization.
 - Example: fetchUrlResponseMetadata: {metadata: "example metadata"}

### webkitFetchMetadata:
 - Description: Metadata from the WebKit fetch operation.
 - Importance: This metadata can provide insights into how the resource was fetched and rendered, which is useful for troubleshooting rendering issues.
 - Example: webkitFetchMetadata: {metadata: "example metadata"}

## GoogleApi.ContentWarehouse.V1.Model.IndexingMobileInterstitialsProtoDesktopInterstitials

### details: 
 - Description: A list of `IndexingMobileInterstitialsProtoDesktopInterstitialsDetails` objects.
 - Importance: This parameter provides detailed information about the desktop interstitials, which can be crucial for understanding specific issues or patterns related to interstitials on a site.
 - Example: `[GoogleApi.ContentWarehouse.V1.Model.IndexingMobileInterstitialsProtoDesktopInterstitialsDetails.t]`

### pipelineEpoch: 
 - Description: The epoch of the interstitial offline pipeline generating this signal.
 - Importance: Knowing the pipeline epoch can help in tracking when the interstitial signal was generated, which is useful for debugging and historical analysis.
 - Example: `"1625097600"`

### pipelinePattern: 
 - Description: Identifies the cluster of URLs for which the signal value was smeared, if present.
 - Importance: This parameter helps in understanding which group of URLs the interstitial signal applies to, aiding in targeted optimizations.
 - Example: `"cluster_123"`

### urlTree: 
 - Description: URL tree of interstitial patterns belonging to the host, used as a site-level signal in Index Signals. It may contain a payload indicating the violated interstitial types.
 - Importance: The URL tree helps in identifying patterns of interstitials across the site, which can be used to improve site-wide SEO strategies.
 - Example: `GoogleApi.ContentWarehouse.V1.Model.IndexingUrlPatternUrlTreeUrlTree.t`

### violatesDesktopInterstitialPolicy: 
 - Description: Indicates the overall policy violation status. If true, at least one of the interstitial signals indicates a violation.
 - Importance: This parameter is critical for compliance with Google's interstitial policies, which can directly impact search rankings.
 - Example: `true`




## GoogleApi.ContentWarehouse.V1.Model.Sitemap

### TargetGroups:
 - Description: One Sitemap can contain multiple TargetGroups, but only one of them will be displayed to the user. This decision will be made at displaying time and can take into account various factors, such as the users' language and country, currently running experiments, etc.
 - Importance: Optimizing TargetGroups can help ensure that the most relevant content is displayed to users based on their specific context, such as language and location. This can improve user experience and potentially increase engagement.
 - Example: A sitemap for an e-commerce site might have different TargetGroups for users in the US and users in the UK, displaying prices in USD and GBP respectively.

### pageAnchorsDocInfo:
 - Description: This field is populated in the Sitemap MDU subpopulator from cdoc data. This is used to store page anchors information for TopicTagsScrolltoFlow.
 - Importance: Storing page anchors information can help improve the navigation and indexing of specific sections within a page, making it easier for users and search engines to find and link to relevant content.
 - Example: A blog post with multiple sections might use page anchors to allow users to jump directly to a specific section, such as "Introduction," "Main Content," and "Conclusion."

### searchInSite:
 - Description: Enable site search.
 - Importance: Enabling site search can improve user experience by allowing users to quickly find specific content within the site. This can also help search engines understand the structure and relevance of the content on the site.
 - Example: A news website might enable site search to allow users to find articles on specific topics or by specific authors.

### sourceOrgfp:
 - Description: Prevents cross-domain forwarding.
 - Importance: Preventing cross-domain forwarding can help maintain the integrity and security of the content, ensuring that users are not redirected to potentially malicious or irrelevant sites.
 - Example: A company website might use sourceOrgfp to ensure that all links remain within the company's domain, preventing users from being redirected to external sites.

### sourceUrl:
 - Description: The original URL of the content.
 - Importance: Including the source URL can help search engines verify the origin of the content, which can be important for indexing and ranking purposes.
 - Example: A syndicated article might include the source URL to indicate where the content was originally published.

### subresultList:
 - Description: This field is populated in the Sitemap MDU subpopulator from cdoc data. It's not set in the cdoc Sitemap.
 - Importance: Populating the subresultList can help organize and display related content, improving the user experience and potentially increasing engagement by providing users with additional relevant content.
 - Example: An online store might use subresultList to display related products or accessories on a product page.

## GoogleApi.ContentWarehouse.V1.Model.RepositoryWebrefDocumentMetadata

### crawlTime: 
 - Description: The timestamp of when the document was crawled (if known). Copied from CompositeDoc.Content.CrawlTime.
 - Importance: Knowing the crawl time can help webmasters understand when their content was last indexed by Google, which can be useful for tracking updates and changes in search rankings.
 - Example: "2023-10-01T12:34:56Z"

### docId: 
 - Description: DocId of the annotated document as read from cdoc.doc().docid().
 - Importance: The DocId is a unique identifier for the document within Google's indexing system, which can be useful for tracking and managing specific documents.
 - Example: "1234567890abcdef"

### forwardingUrls: 
 - Description: URLs that forward to this URL. Needed for URL -> topical entity entries.
 - Importance: Forwarding URLs can help in understanding the redirection paths and can be used to ensure that link equity is properly passed to the final destination URL.
 - Example: ["[http://example.com/old-page](http://example.com/old-page)", "[http://example.com/redirect](http://example.com/redirect)"]

### isDisambiguationPage: 
 - Description: Set to true if the document is a known disambiguation page, e.g., [https://en.wikipedia.org/wiki/Orange](https://en.wikipedia.org/wiki/Orange).
 - Importance: Identifying disambiguation pages can help in understanding the context and intent of the page, which can be useful for improving search relevance.
 - Example: true

### language: 
 - Description: The document language, as read from doc().content().language(). This is go/language-enum value.
 - Importance: Knowing the language of the document is crucial for serving the content to the appropriate audience and for language-specific search optimizations.
 - Example: "en"

### numIncomingAnchors: 
 - Description: The (weighted) number of incoming anchors (links from other documents).
 - Importance: The number of incoming links is a significant factor in determining the authority and relevance of a page, which directly impacts its search ranking.
 - Example: 42

### salientTerms: 
 - Description: The salient terms for this document. Only set if --webref_doc_metadata_copy_salient_terms is true. Same motivation as the title field above.
 - Importance: Salient terms help in understanding the key topics and themes of the document, which can be used to improve keyword targeting and relevance.
 - Example: ["restaurant", "menu", "dining"]

### title: 
 - Description: The title of the document. Only set if --webref_doc_metadata_set_title is true. The idea is that we can use this to more easily learn things like: title contains "restaurants" -> more likely to be a list page.
 - Importance: The title is a critical element for SEO as it directly influences click-through rates and helps search engines understand the content of the page.
 - Example: "Top 10 Restaurants in New York City"

### totalClicks: 
 - Description: The total clicks on this document, taken from navboost data.
 - Importance: The number of clicks can indicate the popularity and user engagement of the document, which can be a factor in search rankings.
 - Example: 1500

### url: 
 - Description: The URL of the document.
 - Importance: The URL is essential for identifying the document on the web and is a fundamental element for SEO and indexing.
 - Example: "[http://example.com/page](http://example.com/page)"




## GoogleApi.ContentWarehouse.V1.Model.IndexingEmbeddedContentEmbeddedContentInfo

### compressedDocumentTrees:
 - Description: The document's DOM and render tree produced by WebKit as a side effect of rendering the page. It might be compressed or not. Thus, use indexing::embedded_content::UncompressWebkitDocument to decode it.
 - Importance: This parameter is crucial for understanding the structure and rendering of the webpage, which can impact how the content is indexed and ranked by the search engine.
 - Example: "compressedDocumentTrees": "compressed_data_string"

### convertedContents:
 - Description: The converted contents, as produced by the same DocumentUpdater transaction that generated the render tree. Useful whenever one of our users wants to experiment with deriving an annotation from the render tree.
 - Importance: This parameter helps in analyzing the content transformations that occur during rendering, which can be useful for optimizing content presentation and improving SEO.
 - Example: "convertedContents": "converted_data_string"

### embeddedLinksInfo:
 - Description: Information about all external resources needed to render this page, a.k.a. embedded links. This includes .css files, images embedded in a page, external javascripts, iframes etc.
 - Importance: Understanding and optimizing embedded links is essential for ensuring that all resources are properly loaded and rendered, which can affect page load times and overall user experience, both of which are important for SEO.
 - Example: "embeddedLinksInfo": { "css_files": ["style.css"], "images": ["image1.png"], "scripts": ["script.js"] }

### headlessResponse:
 - Description: The headless response for rendering the document.
 - Importance: This parameter provides insights into how the page is rendered in a headless browser environment, which can be useful for debugging rendering issues and ensuring that the page is correctly indexed.
 - Example: "headlessResponse": { "status": 200, "content": "rendered_html_content" }

### isAlternateSnapshot:
 - Description: Indicate if the snapshot is generated from alternate snapshot. If true, the snapshot will be exported even if the snapshot quality score is low.
 - Importance: This parameter can help in identifying and optimizing alternate versions of the page, which can be useful for A/B testing and improving the overall quality of the content.
 - Example: "isAlternateSnapshot": true

### originalEncoding:
 - Description: The original encoding of the content crawled from trawler. It's the value of enum i18n::encodings::encoding. We put a int32 here instead of encoding proto to maintain the compatibility of "py_api_version = 1".
 - Importance: Knowing the original encoding is important for correctly interpreting and displaying the content, which can affect how the content is indexed and ranked.
 - Example: "originalEncoding": 5

### referencedResource:
 - Description: Information about all external resources used to render this page, a.k.a. embedded links. This includes .css files, images embedded in a page, external javascripts, iframes etc.
 - Importance: Similar to embeddedLinksInfo, this parameter is crucial for ensuring that all resources are properly loaded and rendered, which can affect page load times and overall user experience.
 - Example: "referencedResource": [{ "type": "css", "url": "style.css" }, { "type": "image", "url": "image1.png" }]

### renderedSnapshot:
 - Description: Only exist in dry run mode.
 - Importance: This parameter can be useful for testing and debugging purposes, allowing webmasters to see how the page would be rendered without actually making it live.
 - Example: "renderedSnapshot": { "image_data": "base64_encoded_image" }

### renderedSnapshotImage:
 - Description: Snapshot image of a rendered html document (possibly encoded as png, jpeg, or webp).
 - Importance: This parameter provides a visual representation of the rendered page, which can be useful for identifying rendering issues and ensuring that the page is displayed correctly.
 - Example: "renderedSnapshotImage": "base64_encoded_image"

### renderedSnapshotMetadata:
 - Description: A collection of values which are needed by the users of the Kodachrome bigtable.
 - Importance: This metadata can provide additional context and information about the rendered snapshot, which can be useful for debugging and optimization purposes.
 - Example: "renderedSnapshotMetadata": { "timestamp": "2023-10-01T12:00:00Z", "quality_score": 0.9 }

### renderedSnapshotQualityScore:
 - Description: The quality of the image, 0.0 is the worst, 1.0 is the best. If all dependencies are successfully crawled, the quality should be 1.0. If one or more of the dependencies are unknown, the quality will be lower.
 - Importance: This score can help in assessing the quality of the rendered page, which can be useful for identifying and addressing issues that may affect the user experience and SEO.
 - Example: "renderedSnapshotQualityScore": 0.85

### richcontentData:
 - Description: The rich content data to recover the original contents from the converted_contents. Useful for offline content analysis.
 - Importance: This parameter can be useful for analyzing and optimizing the content offline, which can help in improving the overall quality and SEO of the page.
 - Example: "richcontentData": { "original_content": "original_html_content" }

## GoogleApi.ContentWarehouse.V1.Model.QualityAuthorityTopicEmbeddingsVersionedItem

### pageEmbedding:
 - Description: Compressed page embeddings.
 - Importance: Page embeddings are crucial for understanding the content and context of individual pages. Optimizing this can help improve how well the search engine understands and ranks the page.
 - Example: "pageEmbedding": "compressed_embedding_string"

### siteEmbedding:
 - Description: Compressed site embeddings.
 - Importance: Site embeddings provide a holistic view of the entire website's content. This helps the search engine understand the overall theme and relevance of the site, which can impact site-wide SEO.
 - Example: "siteEmbedding": "compressed_site_embedding_string"

### siteFocusScore:
 - Description: Number denoting how much a site is focused on one topic.
 - Importance: A higher site focus score indicates that the site is highly specialized in a particular topic, which can improve its authority and ranking for that topic.
 - Example: "siteFocusScore": 0.85

### siteRadius:
 - Description: The measure of how far page_embeddings deviate from the site_embedding.
 - Importance: A smaller site radius indicates that the content of individual pages is closely related to the overall site theme, which can enhance the site's topical authority.
 - Example: "siteRadius": 0.15

### versionId:
 - Description: Identifier for the version of the embeddings.
 - Importance: Keeping track of the version of embeddings can help in maintaining consistency and understanding changes over time, which is important for long-term SEO strategies.
 - Example: "versionId": 3


## GoogleApi.ContentWarehouse.V1.Model.NlpSaftEntityProfile

### canonicalName: 
 - Description: Canonical entity name.
 - Importance: The canonical name is crucial for identifying the primary name of the entity, which helps in ensuring consistency and accuracy in search results.
 - Example: "Google Inc."

### disambiguation: 
 - Description: Disambiguation phrase. The combination of entity name and disambiguation phrase should be unique within the corpus.
 - Importance: This parameter helps in distinguishing between entities with similar names, improving the precision of search results.
 - Example: "Google Inc. (Technology Company)"

### id: 
 - Description: Unique global id for entity.
 - Importance: A unique identifier ensures that each entity can be distinctly recognized and retrieved, which is essential for accurate data management and search indexing.
 - Example: "12345-abcde-67890"

### identifier: 
 - Description: External identifiers for entity.
 - Importance: External identifiers link the entity to other databases or systems, enhancing the entity's credibility and the richness of the information available.
 - Example: ["ISBN:978-3-16-148410-0", "DOI:10.1000/182"]

### mid: 
 - Description: Freebase MID for entity. This field should be the same as FREEBASE_MID identifier for the entity profile.
 - Importance: The Freebase MID provides a standardized identifier that can be used across various platforms, ensuring consistency in entity recognition.
 - Example: "/m/02mjmr"

### name: 
 - Description: Representative name for entity.
 - Importance: The representative name is the primary label used in search results and interfaces, making it critical for user recognition and interaction.
 - Example: "Google"

### nameLanguage: 
 - Description: Language for the name and disambiguation.
 - Importance: Specifying the language ensures that the entity's name and disambiguation are correctly interpreted and displayed in the appropriate linguistic context.
 - Example: "en" (for English)

### type: 
 - Description: Entity type.
 - Importance: Defining the entity type helps in categorizing and filtering search results, improving the relevance and accuracy of the information retrieved.
 - Example: "Organization"

## GoogleApi.ContentWarehouse.V1.Model.CrawlerChangerateUrlChange

### additionalChangesMerged:
 - Description: Duplicate UrlChanges crawled within a specified time range will be merged together. UrlChanges are considered duplicates if the simhash, simhash_is_trusted, simhash_v2, simhash_v2_is_trusted, and shingle_simhash are the same. additional_changes_merged indicates the number of duplicate UrlChanges merged into this UrlChange.
 - Importance: This parameter helps in reducing redundancy by merging duplicate changes, which can optimize storage and processing efficiency.
 - Example: If 5 duplicate UrlChanges are detected, additionalChangesMerged would be 4.

### interval:
 - Description: The length in seconds of the change.
 - Importance: This parameter indicates the duration of the change, which can be useful for understanding the frequency and timing of content updates.
 - Example: If a change lasted for 3600 seconds, interval would be 3600.

### offDomainLinksChange:
 - Description: Whether the content of the off-domain links changed.
 - Importance: This parameter helps in tracking changes in external links, which can affect the site's link profile and potentially its SEO.
 - Example: If off-domain links changed, offDomainLinksChange would be true.

### offDomainLinksCount:
 - Description: The new count of off-domain links, if they changed.
 - Importance: This parameter provides the updated number of external links, which can be important for link analysis and SEO strategies.
 - Example: If the number of off-domain links changed to 10, offDomainLinksCount would be 10.

### onDomainLinksCount:
 - Description: The new count of on-domain links, if the count changed.
 - Importance: This parameter provides the updated number of internal links, which can be important for internal linking strategies and SEO.
 - Example: If the number of on-domain links changed to 20, onDomainLinksCount would be 20.

### onDomainLinksCountChange:
 - Description: Whether the number of on-domain links changed.
 - Importance: This parameter helps in tracking changes in internal links, which can affect site navigation and SEO.
 - Example: If the number of on-domain links changed, onDomainLinksCountChange would be true.

### simhashV2:
 - Description: The simhash-v2 value.
 - Importance: This parameter is used for detecting duplicate content and changes in content, which is crucial for content indexing and SEO.
 - Example: A specific simhashV2 value might look like "3f4a9b8c".

### simhashV2IsTrusted:
 - Description: Whether the simhash-v2 value should be trusted.
 - Importance: This parameter indicates the reliability of the simhash-v2 value, which can affect the accuracy of content change detection.
 - Example: If the simhash-v2 value is reliable, simhashV2IsTrusted would be true.




## GoogleApi.ContentWarehouse.V1.Model.CrawlerChangerateUrlVersion

### contentType: 
 - Description: The content type of the page.
 - Importance: The content type helps search engines understand the nature of the content on the page, which can influence how the page is indexed and ranked. For example, distinguishing between HTML, PDF, or image content can affect how the content is processed and displayed in search results.
 - Example: "text/html", "application/pdf"

### lastModified: 
 - Description: The date from the LastModified header, if present.
 - Importance: The last modified date helps search engines determine the freshness of the content. More recent content can be prioritized in search results, and knowing when a page was last updated can help in assessing its relevance and accuracy.
 - Example: 1672531199 (Unix timestamp)

### simhashV2: 
 - Description: The simhash-v2 value.
 - Importance: Simhash is used to detect duplicate content by generating a fingerprint of the page's content. Simhash-v2 is the updated version, and using it helps in accurately identifying and handling duplicate content, which is crucial for maintaining the quality of search results.
 - Example: "3f4a9b8c"

### timestamp: 
 - Description: The timestamp we crawled the page.
 - Importance: The crawl timestamp indicates when the page was last crawled by the search engine. This information is important for understanding the recency of the data and can influence how often the page is revisited and re-indexed.
 - Example: 1672531199 (Unix timestamp)

## GoogleApi.ContentWarehouse.V1.Model.QualityPreviewRanklabTitle

### perTypeRank:
 - Description: Rank of this title among titles of the same data_source_type.
 - Importance: This parameter helps in understanding the relative ranking of a title within its specific data source type, which can be crucial for optimizing title selection and improving search engine ranking.
 - Example: If a title has a perTypeRank of 1, it means it is the highest-ranked title among its data source type.

### queryMatch:
 - Description: The number of (different) terms with a query match. It may include the match with any SQuery node (e.g., synonyms).
 - Importance: This parameter indicates how well the title matches the search query, which is essential for relevance and improving click-through rates.
 - Example: A queryMatch value of 3 means that three different terms in the title match the search query.

### percentBodyTitleTokensCovered:
 - Description: Numbers of body title tokens covered by this title, in range of [0, 1]. Not set if body title is considered "bad".
 - Importance: This parameter measures the extent to which the title covers the content of the body, which can be important for ensuring that the title accurately represents the page content.
 - Example: A percentBodyTitleTokensCovered value of 0.8 means that 80% of the body title tokens are covered by this title.

### hasSiteInfo:
 - Description: Whether a title contains site information.
 - Importance: Including site information in the title can improve brand recognition and trustworthiness, which can positively impact user engagement and SEO.
 - Example: A title with hasSiteInfo set to true might include the site name or domain in the title.

### isValid:
 - Description: Whether a title is valid (i.e., not empty).
 - Importance: Ensuring that titles are valid and not empty is fundamental for SEO, as empty titles can negatively impact search engine rankings and user experience.
 - Example: A title with isValid set to true is a non-empty, properly formatted title.

### queryMatchFraction:
 - Description: A number of matched query terms divided by the number of all terms in query. Synonyms or other terms that appear in squery but not in the raw query are excluded. Takes values in [0, 1].
 - Importance: This parameter provides a normalized measure of how well the title matches the search query, which is important for relevance scoring and improving search engine ranking.
 - Example: A queryMatchFraction value of 0.5 means that 50% of the query terms are matched by the title.

### widthFraction:
 - Description: A rendered width of this title divided by the max allowed width for title. Takes values in [0, 1].
 - Importance: This parameter helps in ensuring that the title fits within the allowed display width, which is important for maintaining readability and user experience.
 - Example: A widthFraction value of 0.9 means that the title occupies 90% of the maximum allowed width.

### goldminePageScore:
 - Description: The score for the text computed in Goldmine (AlternativeTitlesAnnotator).
 - Importance: This score is used to evaluate the quality of the title, which can be crucial for selecting the best title for SEO purposes.
 - Example: A goldminePageScore of 85 indicates a high-quality title according to the Goldmine scoring system.

### goldmineAdjustedScore:
 - Description: The score for text computed in Goldmine (AlternativeTitlesAnnotator) with additional scoring adjustments applied. Currently includes Blockbert scoring.
 - Importance: This adjusted score provides a more refined evaluation of the title's quality, incorporating additional factors that can impact SEO.
 - Example: A goldmineAdjustedScore of 90 indicates a very high-quality title after adjustments.

### docLang:
 - Description: Document language for this title. It is used for model inference and hence flattened into RanklabTitle instead of RanklabDoc.
 - Importance: Specifying the document language is important for ensuring that the title is correctly interpreted and ranked by language-specific search algorithms.
 - Example: A docLang value of "en" indicates that the document language is English.

## GoogleApi.ContentWarehouse.V1.Model.QualityNavboostCrapsFeatureCrapsData

### country:
 - Description: Country, like "us". If not present, it's an aggregation for all countries. This is the same format as one used in Glue.
 - Importance: Specifying the country can help in targeting and optimizing content for specific geographic regions, which can improve local SEO performance.
 - Example: "us"

### device:
 - Description: Device, like "m". If not present, it's an aggregation for all devices. "m" - mobile devices. "d" - desktop devices.
 - Importance: Differentiating between mobile and desktop devices allows for device-specific optimizations, which can enhance user experience and improve rankings on device-specific searches.
 - Example: "m"

### language:
 - Description: Language, like "en". If not present, it's an aggregation for all languages. This is the same format as one used in Glue.
 - Importance: Specifying the language helps in targeting content to users who speak that language, which can improve relevance and SEO for language-specific queries.
 - Example: "en"

### locationId:
 - Description: Location id for metro and city. If not present, it's an aggregation for all locations within the current country.
 - Importance: Targeting specific metro and city locations can enhance local SEO efforts, making the content more relevant to users in those specific areas.
 - Example: 12345

### signals:
 - Description: CRAPS Signals for the locale.
 - Importance: These signals can provide insights into user interactions and behaviors, which can be used to optimize content and improve its relevance and ranking.
 - Example: GoogleApi.ContentWarehouse.V1.Model.QualityNavboostCrapsCrapsClickSignals.t

### voterTokenBitmap:
 - Description: The set of voter tokens of the sessions that contributed to this feature's stats. Voter tokens are not unique per user, so it is a lower bound on the number of distinct users. Used for privacy-related filtering.
 - Importance: Understanding the number of distinct user sessions can help in assessing the popularity and engagement of the content, which can inform optimization strategies.
 - Example: GoogleApi.ContentWarehouse.V1.Model.QualityNavboostGlueVoterTokenBitmapMessage.t




## GoogleApi.ContentWarehouse.V1.Model.QualityNavboostCrapsCrapsData

### country:
 - Description: The two-letter uppercase country slice of the CrapsData.
 - Importance: This parameter helps in segmenting data based on the country, which can be crucial for understanding regional performance and optimizing content for specific geographic locations.
 - Example: "US", "FR", "BR"

### device:
 - Description: The device interface and OS slice of the CrapsData.
 - Importance: Understanding the device and OS can help in optimizing the website for different devices, ensuring better user experience and potentially higher rankings.
 - Example: GoogleApi.ContentWarehouse.V1.Model.QualityNavboostCrapsCrapsDevice.t

### features:
 - Description: Contains CrapsClickSignals for specific features.
 - Importance: This parameter allows for the analysis of specific features' performance, which can be used to optimize those features for better user engagement.
 - Example: list(GoogleApi.ContentWarehouse.V1.Model.QualityNavboostCrapsFeatureCrapsData.t)

### language:
 - Description: The language slice of the CrapsData.
 - Importance: Segmenting data by language helps in optimizing content for different linguistic groups, improving accessibility and relevance.
 - Example: "en", "fr", "pt-BR"

### patternLevel:
 - Description: Level of pattern. More general patterns get higher values.
 - Importance: Understanding the pattern level helps in identifying and optimizing URL structures, which can improve crawl efficiency and indexing.
 - Example: For URL "[http://abc.def.ghi/xyz.html](http://abc.def.ghi/xyz.html)", level 0 pattern will be "[http://abc.def.ghi/xyz.html](http://abc.def.ghi/xyz.html)", level 1 pattern will be "p://abc.def.ghi", level 2 pattern will be "p://def.ghi"

### sliceTag:
 - Description: This field can be used by the craps pipeline to slice up signals by various attributes such as device type, country, locale etc.
 - Importance: The sliceTag allows for detailed segmentation of data, enabling more precise optimizations based on specific attributes.
 - Example: An arbitrary string representing a specific slice, such as "mobile_US_en"

### voterTokenCount:
 - Description: The number of distinct voter tokens (a lower bound on the number of distinct users that contributed to the entry, used for privacy-related filtering).
 - Importance: This parameter helps in understanding the diversity of user interactions, which can be important for privacy considerations and ensuring a broad user base.
 - Example: An integer value representing the count of distinct voter tokens.




## GoogleApi.ContentWarehouse.V1.Model.CompressedQualitySignals

### ugcDiscussionEffortScore:
 - Description: UGC page quality signals. (Times 1000 and floored).
 - Importance: This parameter indicates the quality of user-generated content (UGC) on a page, which can affect the page's ranking in search results.
 - Example: A high ugcDiscussionEffortScore might indicate that the page has high-quality user discussions, which can be a positive signal for search ranking.

### productReviewPPromotePage:
 - Description: Product review promotion confidence. (Times 1000 and floored).
 - Importance: This parameter helps in promoting pages with high-quality product reviews, which can improve their visibility in search results.
 - Example: A high productReviewPPromotePage score can boost the ranking of a page with detailed and helpful product reviews.

### productReviewPDemoteSite:
 - Description: Product review demotion confidence. (Times 1000 and floored).
 - Importance: This parameter helps in demoting sites with low-quality product reviews, which can negatively impact their search ranking.
 - Example: A high productReviewPDemoteSite score can lower the ranking of a site with spammy or unhelpful product reviews.

### exactMatchDomainDemotion:
 - Description: Page quality signals converted from fields in proto QualityBoost in quality/q2/proto/quality-boost.proto. To save indexing space, float values in [0, 1] are converted to integers in range [0, 1023] (use 10 bits). exact_match_domain_demotion: converted from QualityBoost.emd.boost.
 - Importance: This parameter helps in demoting pages that rely heavily on exact match domains, which can be a sign of low-quality or manipulative SEO practices.
 - Example: A high exactMatchDomainDemotion score can lower the ranking of a page that uses exact match domains excessively.

### lowQuality:
 - Description: S2V low quality score: converted from quality_nsr.NsrData, applied in Qstar.
 - Importance: This parameter indicates the overall low quality of a page, which can negatively impact its ranking.
 - Example: A high lowQuality score can demote a page that has poor content quality or user experience.

### navDemotion:
 - Description: nav_demotion: converted from QualityBoost.nav_demoted.boost.
 - Importance: This parameter helps in demoting pages with poor navigation, which can affect user experience and search ranking.
 - Example: A high navDemotion score can lower the ranking of a page with confusing or difficult navigation.

### siteAuthority:
 - Description: site_authority: converted from quality_nsr.SiteAuthority, applied in Qstar.
 - Importance: This parameter indicates the authority of a site, which can positively impact its ranking in search results.
 - Example: A high siteAuthority score can boost the ranking of a site that is considered authoritative in its niche.

### babyPandaV2Demotion:
 - Description: New BabyPanda demotion, applied on top of Panda. This is meant to replace |baby_panda_demotion|.
 - Importance: This parameter helps in demoting low-quality content, which can improve the overall quality of search results.
 - Example: A high babyPandaV2Demotion score can lower the ranking of a page with thin or low-quality content.

### authorityPromotion:
 - Description: authority promotion: converted from QualityBoost.authority.boost.
 - Importance: This parameter helps in promoting authoritative pages, which can improve their visibility in search results.
 - Example: A high authorityPromotion score can boost the ranking of a page that is considered a reliable source of information.

### productReviewPUhqPage:
 - Description: The possibility of a page being a high-quality review page.
 - Importance: This parameter helps in identifying and promoting high-quality product review pages, which can improve their search ranking.
 - Example: A high productReviewPUhqPage score can boost the ranking of a page with detailed and well-written product reviews.

### scamness:
 - Description: Scam model score. Used as one of the web page quality qstar signals. Value range from 0 to 1023.
 - Importance: This parameter helps in identifying and demoting scammy or fraudulent pages, which can improve the overall quality of search results.
 - Example: A high scamness score can lower the ranking of a page that is identified as potentially scammy.

### unauthoritativeScore:
 - Description: Unauthoritative score. Used as one of the web page quality qstar signals.
 - Importance: This parameter helps in demoting pages that are considered unauthoritative, which can negatively impact their search ranking.
 - Example: A high unauthoritativeScore can lower the ranking of a page that lacks credibility or authority.

### productReviewPReviewPage:
 - Description: The possibility of a page being a review page.
 - Importance: This parameter helps in identifying and promoting review pages, which can improve their visibility in search results.
 - Example: A high productReviewPReviewPage score can boost the ranking of a page that contains product reviews.

### serpDemotion:
 - Description: serp demotion: applied in Qstar.
 - Importance: This parameter helps in demoting pages that perform poorly in search engine results pages (SERPs), which can negatively impact their ranking.
 - Example: A high serpDemotion score can lower the ranking of a page that has a high bounce rate or low click-through rate in SERPs.

### anchorMismatchDemotion:
 - Description: anchor_mismatch_demotion: converted from QualityBoost.mismatched.boost.
 - Importance: This parameter helps in demoting pages with mismatched anchor text, which can be a sign of manipulative SEO practices.
 - Example: A high anchorMismatchDemotion score can lower the ranking of a page that uses misleading or irrelevant anchor text.

### pandaDemotion:
 - Description: This is the encoding of Panda fields in the proto SiteQualityFeatures in quality/q2/proto/site_quality_features.proto. The encoding/decoding is performed using functions from quality_coati::coati_util.
 - Importance: This parameter helps in demoting low-quality content, which can improve the overall quality of search results.
 - Example: A high pandaDemotion score can lower the ranking of a page with thin or low-quality content.

### productReviewPDemotePage:
 - Description: Product review demotion confidence. (Times 1000 and floored).
 - Importance: This parameter helps in demoting pages with low-quality product reviews, which can negatively impact their search ranking.
 - Example: A high productReviewPDemotePage score can lower the ranking of a page with spammy or unhelpful product reviews.

## GoogleApi.ContentWarehouse.V1.Model.QualityNavboostCrapsCrapsClickSignals

### absoluteImpressions
 - Description: This field is used for host level unsquashed impressions. When compressed, this value is represented individually and is generally incompatible with other values compressed as click-ratios.
 - Importance: Understanding absolute impressions can help webmasters gauge the raw number of times their content is viewed without any compression or ratio adjustments, providing a clearer picture of visibility.
 - Example: If a webpage has 1000 absolute impressions, it means it was viewed 1000 times in its raw form.

### unicornClicks
 - Description: The subset of clicks that are associated with an event from a Unicorn user.
 - Importance: Identifying unicorn clicks can help webmasters understand the engagement from a specific subset of users, which might be more valuable or targeted.
 - Example: If a webpage has 50 unicorn clicks, it means 50 clicks came from Unicorn users.

### unsquashedClicks
 - Description: This field is not being populated for the current format; instead, two instances of CrapsClickSignals (squashed/unsquashed) are used. It will be populated in the new format.
 - Importance: Tracking unsquashed clicks can provide a more detailed and uncompressed view of user engagement, which can be crucial for accurate analysis.
 - Example: If a webpage has 200 unsquashed clicks, it means 200 clicks were recorded in their raw form.

### unsquashedImpressions
 - Description: This field is not being populated for the current format; instead, two instances of CrapsClickSignals (squashed/unsquashed) are used. It will be populated in the new format.
 - Importance: Monitoring unsquashed impressions can help webmasters understand the true reach of their content without any compression, aiding in more precise visibility metrics.
 - Example: If a webpage has 1500 unsquashed impressions, it means it was viewed 1500 times in its raw form.

### unsquashedLastLongestClicks
 - Description: This field is not being populated for the current format; instead, two instances of CrapsClickSignals (squashed/unsquashed) are used. It will be populated in the new format.
 - Importance: Tracking unsquashed last longest clicks can provide insights into the most significant user interactions in their raw form, which can be critical for understanding user behavior.
 - Example: If a webpage has 30 unsquashed last longest clicks, it means 30 significant clicks were recorded in their raw form.

## GoogleApi.ContentWarehouse.V1.Model.CompositeDocIndexingInfo

### cdocBuildInfo:
 - Description: To hold extra info for building a final cdoc from raw cdoc and goldmine annotations.
 - Importance: This parameter is crucial for the accurate construction of the final composite document (cdoc) from raw data and annotations, ensuring the integrity and completeness of the indexed content.
 - Example: `cdocBuildInfo: %GoogleApi.ContentWarehouse.V1.Model.IndexingDocjoinerCDocBuildInfo{}`

### contentProtected:
 - Description: Whether the current page is under content protection, i.e., a page has been crawled as an error page, but its last known good content is preserved, and its crawl_status is kept as converter.CrawlStatus::CONTENT.
 - Importance: This parameter helps in maintaining the integrity of the content by preserving the last known good version of a page that encountered errors during crawling.
 - Example: `contentProtected: true`

### convertToRobotedReason:
 - Description: If set, indicates that the crawl status was converted to ROBOTED for the reason specified by the enum value in converter.RobotedReasons.ConvertToRobotedReasons.
 - Importance: This parameter is important for understanding why a document's crawl status was changed to ROBOTED, which can affect its visibility in search results.
 - Example: `convertToRobotedReason: 1`

### crawlStatus:
 - Description: One of the enum values in converter.CrawlStatus.State. Default is converter.CrawlStatus::CONTENT. The document is roboted if the value is converter.CrawlStatus::ROBOTED.
 - Importance: This parameter indicates the current crawl status of the document, which is essential for determining its eligibility for indexing and serving.
 - Example: `crawlStatus: 2`

### errorType:
 - Description: One of the enum values in converter.ErrorPageType. Default is converter::ERROR_PAGE_NONE.
 - Importance: This parameter helps in identifying the type of error encountered during the crawling process, which can be useful for debugging and improving crawl efficiency.
 - Example: `errorType: 0`

### hostid:
 - Description: The host id of the document. Used chiefly to determine whether the document is part of a parked domain.
 - Importance: This parameter is important for identifying the hosting domain of the document, which can influence its ranking and indexing.
 - Example: `hostid: "example.com"`

### indexingTs:
 - Description: The timestamp (the time since the Epoch, in microseconds) when the docjoin is exported from indexing.
 - Importance: This parameter is used to identify different versions of the same document, which is crucial for version control and ensuring the most recent content is indexed.
 - Example: `indexingTs: "1622547800000000"`

### noLongerCanonicalTimestamp:
 - Description: If set, the timestamp in microseconds when the URL stopped being canonical.
 - Importance: This parameter prevents the deletion of old documents until the new canonical document is picked up, ensuring continuity and accuracy in indexing.
 - Example: `noLongerCanonicalTimestamp: "1622547800000000"`

### normalizedClickScore:
 - Description: This score is calculated by re-mapping the back onto the partition's score distribution, representing the score of the equivalently ranked organically-selected document.
 - Importance: This parameter helps in understanding the relative popularity and relevance of a document based on user interactions.
 - Example: `normalizedClickScore: 0.85`

### primaryVertical:
 - Description: Vertical membership of the document. Indicates the vertical that initiated indexing of this document.
 - Importance: This parameter helps in categorizing the document within specific verticals, which can influence its ranking and visibility in vertical-specific searches.
 - Example: `primaryVertical: "news"`

### rawNavboost:
 - Description: The raw navboost count for the canonical URL without aggregating the navboost from duplicate URLs.
 - Importance: This parameter is used when building the forwarding map, which can affect the document's ranking and navigation efficiency.
 - Example: `rawNavboost: 5`

### rowTimestamp:
 - Description: The timestamp (the time since the Epoch, in microseconds) to represent the document version, used in downstream processing after Raffia.
 - Importance: This parameter ensures that the most recent version of the document is used in processing and storage, maintaining data accuracy.
 - Example: `rowTimestamp: "1622547800000000"`

### selectionTierRank:
 - Description: Selection tier rank is a language normalized score ranging from 0-1 over the serving tier for this document.
 - Importance: This parameter helps in ranking the document within its serving tier, influencing its visibility and priority in search results.
 - Example: `selectionTierRank: 0.75`

### tracingId:
 - Description: The tracing IDs label the version of the URL for URL status tracking.
 - Importance: This parameter is used for tracking the status and changes of URLs, which is important for monitoring and debugging indexing processes.
 - Example: `tracingId: ["id1", "id2"]`

### urlChangerate:
 - Description: Changerate information for this document.
 - Importance: This parameter provides insights into how frequently the document's URL changes, which can affect its stability and ranking.
 - Example: `urlChangerate: %GoogleApi.ContentWarehouse.V1.Model.CrawlerChangerateUrlChangerate{}`

### urlHistory:
 - Description: URL change history for this document.
 - Importance: This parameter helps in understanding the document's URL changes over time, which can be useful for tracking its evolution and stability.
 - Example: `urlHistory: %GoogleApi.ContentWarehouse.V1.Model.CrawlerChangerateUrlHistory{}`

### urlPatternSignals:
 - Description: UrlPatternSignals for this document, used to compute document score in LTG.
 - Importance: This parameter is used to compute the document's score based on URL patterns, influencing its ranking and relevance.
 - Example: `urlPatternSignals: %GoogleApi.ContentWarehouse.V1.Model.IndexingSignalAggregatorUrlPatternSignals{}`

### videoIndexingInfo:
 - Description: Indexing info about videos.
 - Importance: This parameter provides information about video content, which is important for indexing and ranking video documents.
 - Example: `videoIndexingInfo: %GoogleApi.ContentWarehouse.V1.Model.ImageRepositoryVideoIndexingInfo{}`




## GoogleApi.ContentWarehouse.V1.Model.GDocumentBase

### DisplayUrl:
 - Description: Sometimes the URL displayed in search results should be different from what gets indexed (e.g. in enterprise, content management systems). If this value is not set, we default to the regular URL.
 - Importance: Optimizing the DisplayUrl can help ensure that the most user-friendly and relevant URL is shown in search results, which can improve click-through rates.
 - Example: "[https://example.com/user-friendly-url](https://example.com/user-friendly-url)"

### NoIndexReason:
 - Description: When these reasons are set to a non-zero value, the document should not be indexed, or show a snippet, or show a cache, etc. These reasons are bit maps of indexing.converter.RobotsInfo.RobotedReasons enum values reflecting the places where the restriction was found.
 - Importance: Ensuring that NoIndexReason is correctly set can prevent unwanted pages from being indexed, which can help maintain the quality and relevance of the indexed content.
 - Example: 1 (indicating a specific reason for no-indexing)

### PagerankNS:
 - Description: Pagerank-NearestSeeds is a pagerank score for the doc, calculated using NearestSeeds method. This is the production PageRank value teams should use.
 - Importance: PagerankNS is a critical metric for understanding the importance and authority of a document within the search engine's index, which can influence its ranking in search results.
 - Example: 5 (indicating a higher PageRank score)

### URL:
 - Description: The URL does NOT uniquely identify a document ANYMORE. For a unique identifier across all documents in production please refer to the field 'id().key()' listed above. Reason: foo.bar:/http and foo.bar:/http:SMARTPHONE share the same URL, but the body of the two documents might differ because of different crawl-context (desktop vs. smartphone in this example).
 - Importance: Ensuring the correct URL is used and understanding its limitations can help in managing duplicate content and ensuring the right version of a page is indexed.
 - Example: "[https://example.com/page](https://example.com/page)"

### URLAfterRedirects:
 - Description: The final URL after all redirects have been followed.
 - Importance: This parameter is important for understanding the actual destination of a URL, which can help in managing redirects and ensuring the correct page is indexed.
 - Example: "[https://example.com/final-destination](https://example.com/final-destination)"

### userAgentName:
 - Description: The user agent name used to crawl the URL. This field is copied from the first WEBMIRROR FetchReplyClientInfo in trawler_fetch_info column.
 - Importance: Knowing the user agent that crawled the URL can help in understanding how the page was accessed and ensuring that the correct user agent is used for crawling.
 - Example: "GoogleBot"



## GoogleApi.ContentWarehouse.V1.Model.AnchorsAnchorSource

### additionalInfo:
 - Description: Additional information related to the source, such as news hub info.
 - Importance: This parameter can provide context about the source, which may be useful for understanding the relevance and authority of the link.
 - Example: {"newsHubInfo": "example_info"}

### compressedUrl:
 - Description: Compressed source URL.
 - Importance: This parameter helps in reducing the storage space required for URLs, which can be beneficial for large-scale data processing and retrieval.
 - Example: "[http://compressed.url/example](http://compressed.url/example)"

### crawlTimestamp:
 - Description: Source page crawl timestamp.
 - Importance: Indicates the freshness of the content, which is crucial for search engines to determine the relevance and timeliness of the information.
 - Example: "2023-10-01T12:34:56Z"

### docid:
 - Description: The document ID, which is required when anchors are stored as part of docjoin files in the segment indexer.
 - Importance: Essential for identifying and retrieving the specific document within the search engine's index.
 - Example: "1234567890"

### homePageInfo:
 - Description: Information about if the source page is a home page. It can be one of the enum values defined in PerDocData::HomePageInfo (NOT_HOMEPAGE, NOT_TRUSTED, PARTIALLY_TRUSTED, and FULLY_TRUSTED).
 - Importance: Helps in assessing the trustworthiness and importance of the source page, which can influence ranking.
 - Example: "FULLY_TRUSTED"

### indyrank:
 - Description: Independent rank on a uint16 scale.
 - Importance: Provides an additional metric for evaluating the importance and relevance of the source page.
 - Example: 500

### language:
 - Description: Language of the source page, default is English.
 - Importance: Important for ensuring that the content is served to users in the appropriate language, enhancing user experience and relevance.
 - Example: 1 (for English)

### linkhash:
 - Description: Hash of the link.
 - Importance: Used for efficiently identifying and managing links within the search engine's database.
 - Example: "abcdef123456"

### localCountryCodes:
 - Description: Countries to which the source page is local/most relevant; stored as III identifiers for country/region codes.
 - Importance: Helps in geo-targeting and serving content that is most relevant to users in specific regions.
 - Example: [840, 124] (for USA and Canada)

### nsr:
 - Description: NSR value with a range [0,1000], representing the original value [0.0,1.0] multiplied by 1000 and rounded to an integer.
 - Importance: Provides a normalized score for ranking purposes, aiding in the evaluation of the source page's quality.
 - Example: 750

### outdegree:
 - Description: Number of outgoing links from the source page.
 - Importance: Indicates the connectivity and potential authority of the source page, which can impact its ranking.
 - Example: 25

### outsites:
 - Description: Approximate number of pointed-to sites.
 - Importance: Helps in understanding the breadth of the source page's linking behavior, which can influence its perceived authority.
 - Example: 10

### packedIpaddress:
 - Description: String in IPAddress::ToPackedString() format.
 - Importance: Useful for identifying the source server's location and managing IP-based data.
 - Example: "192.0.2.1"

### pagerank:
 - Description: PageRank on a uint16 scale.
 - Importance: A key metric for determining the importance and authority of the source page within the web's link structure.
 - Example: 800

### pagerankNs:
 - Description: PageRank in a normalized scale.
 - Importance: Provides a standardized measure of the source page's importance, aiding in consistent ranking.
 - Example: 750

### spamrank:
 - Description: Spam rank on a uint16 scale.
 - Importance: Helps in identifying and filtering out low-quality or spammy content, ensuring higher quality search results.
 - Example: 100

### spamscore2:
 - Description: Spam score on a 0-127 scale.
 - Importance: Provides an additional metric for evaluating the likelihood of the source page being spam, aiding in maintaining search result quality.
 - Example: 20

### webtableKey:
 - Description: Webtable key of the source.
 - Importance: Essential for efficiently locating and managing the source page within the search engine's database.
 - Example: "webtable_key_example"

## GoogleApi.ContentWarehouse.V1.Model.CompositeDoc

### localizedAlternateName:
 - Description: Localized alternate names are similar to alternate names, except that it is associated with a language different from its canonical. This is the subset of webmaster-provided localized alternate names being in the dup cluster of this document. Used during serving for swapping in the URL based on regional and language preferences of the user.
 - Importance: Optimizing this parameter can help ensure that the correct localized version of a URL is served to users based on their regional and language preferences, improving user experience and potentially increasing engagement.
 - Example: A website with an English canonical name might have a localized alternate name in Spanish for users in Spain.

### badSslCertificate:
 - Description: This field is present if the page has a bad SSL certificate itself or in its redirect chain.
 - Importance: Ensuring that this parameter is not flagged is crucial for maintaining user trust and search engine ranking, as sites with bad SSL certificates may be penalized or flagged as unsafe.
 - Example: A website with an expired SSL certificate would have this field present.

### richcontentData:
 - Description: If present, indicates that some content was inserted, deleted, or replaced in the document's content, and stores information about what was inserted, deleted, or replaced.
 - Importance: Keeping this parameter optimized ensures that the search engine has the most accurate and up-to-date content, which can improve indexing and ranking.
 - Example: A blog post where new paragraphs were added and old ones were removed.

### docVideos:
 - Description: Info about videos embedded in the document.
 - Importance: Including relevant video information can enhance the document's richness and improve its chances of appearing in video search results, thereby increasing visibility.
 - Example: A product page with an embedded video tutorial.

### docImages:
 - Description: Info about "selected" images associated with the document for which ImageData is already available. Only images within doc_images where is_indexed_by_imagesearch is true will be selected for indexing.
 - Importance: Ensuring that images are properly indexed can improve the document's visibility in image search results, driving more traffic.
 - Example: A news article with selected images that are indexed by image search.

### urldate:
 - Description: Date in the URL extracted by quality/snippets/urldate/date-in-url.cc. This is given as midnight GMT on the date in question.
 - Importance: Having a clear and accurate date in the URL can help search engines understand the timeliness and relevance of the content, which can impact ranking.
 - Example: A news article URL containing the publication date.

### richsnippet:
 - Description: Rich snippet extracted from the content of a document.
 - Importance: Rich snippets can enhance search result listings by providing additional context, which can improve click-through rates.
 - Example: A recipe page with a rich snippet showing cooking time and ingredients.

### sitemap:
 - Description: Sitelinks: a collection of interesting links a user might be interested in, given they are interested in this document.
 - Importance: Properly structured sitelinks can improve site navigation and user experience, potentially leading to better engagement and lower bounce rates.
 - Example: A homepage with sitelinks to popular sections like "About Us," "Services," and "Contact."

### robotsinfolist:
 - Description: Information related to robots.txt directives for the document.
 - Importance: Ensuring that the robots.txt directives are correctly set can help control how search engines crawl and index the site, which is crucial for SEO.
 - Example: A robots.txt file that disallows crawling of certain private sections of a website.

### csePagerankCutoff:
 - Description: URL should only be selected for CSE Index if its pagerank is higher than cse_pagerank_cutoff.
 - Importance: Ensuring that URLs meet the pagerank cutoff can help in maintaining a high-quality index, which can improve the overall search experience.
 - Example: A high-authority blog post that meets the pagerank criteria for inclusion in the CSE Index.

## GoogleApi.ContentWarehouse.V1.Model.QualityNsrNsrData

### titlematchScore:
 - Description: Titlematch score of the site, a signal that tells how well titles are matching user queries.
 - Importance: This parameter is crucial for SEO as it directly impacts how well the titles of a site match user queries, which can influence click-through rates and search rankings.
 - Example: A high titlematchScore indicates that the titles on the site are well-aligned with common user queries, improving visibility in search results.

### smallPersonalSite:
 - Description: Score of small personal site promotion.
 - Importance: This parameter can help in promoting small personal blogs, which might otherwise be overshadowed by larger sites. Optimizing this score can help small sites gain more visibility.
 - Example: A higher smallPersonalSite score can lead to better promotion and ranking of personal blogs.

### siteAutopilotScore:
 - Description: Aggregated value of URL autopilot scores for this sitechunk.
 - Importance: This score reflects the automated quality assessment of URLs within a site chunk, which can influence the overall site quality perception by the search engine.
 - Example: A higher siteAutopilotScore indicates better automated quality assessment, potentially leading to higher rankings.

### isVideoFocusedSite:
 - Description: Bit to determine whether the site has mostly video content, but is not hosted on any known video-hosting domains.
 - Importance: Identifying a site as video-focused can help in optimizing video content for better search visibility and user engagement.
 - Example: A site with more than 50% of URLs containing watch pages would have this bit set to true.

### chromeInTotal:
 - Description: Site-level Chrome views.
 - Importance: This parameter indicates the number of views a site receives from Chrome users, which can be a signal of site popularity and user engagement.
 - Example: A higher chromeInTotal value suggests higher user engagement and popularity.

### localityScore:
 - Description: Locality score of the site, i.e., the locality component of the LocalAuthority signal.
 - Importance: This score is important for local SEO, as it indicates how well the site is optimized for local search queries.
 - Example: A higher localityScore can improve the site's visibility in local search results.

### siteLinkOut:
 - Description: Aggregated value of URL link out scores for this sitechunk.
 - Importance: This parameter reflects the quality and relevance of outbound links from the site, which can influence the site's authority and trustworthiness.
 - Example: A higher siteLinkOut score indicates better quality and relevance of outbound links.

### siteLinkIn:
 - Description: Average value of the site_link_in for pages in the sitechunk.
 - Importance: This score indicates the quality and quantity of inbound links to the site, which is a critical factor in search engine ranking algorithms.
 - Example: A higher siteLinkIn score suggests better link-building efforts and higher site authority.

### sitePr:
 - Description: PageRank score of the site.
 - Importance: PageRank is a well-known metric used by Google to rank web pages based on their importance and quality. Optimizing this score can significantly impact search rankings.
 - Example: A higher sitePr score indicates a higher perceived importance and quality of the site.

### impressions:
 - Description: Site-level impressions.
 - Importance: This parameter indicates how often the site appears in search results, which can be a measure of its visibility and relevance.
 - Example: A higher number of impressions suggests better visibility in search results.

### spambrainLavcScore:
 - Description: The SpamBrain LAVC score, as of July 2022.
 - Importance: This score helps in identifying and mitigating spammy content, which is crucial for maintaining site quality and avoiding penalties.
 - Example: A lower spambrainLavcScore indicates better compliance with quality guidelines and less spammy content.

### articleScore:
 - Description: Score from article classification of the site.
 - Importance: This score reflects the quality and relevance of articles on the site, which can influence content ranking and user engagement.
 - Example: A higher articleScore indicates better quality and relevance of the site's articles.

### videoScore:
 - Description: Score indicating the quality of video content on the site.
 - Importance: This parameter is important for sites with video content, as it can influence the ranking and visibility of video pages.
 - Example: A higher videoScore suggests better quality and relevance of video content.

### healthScore:
 - Description: Categorical signals related to the health content of the site.
 - Importance: This score is crucial for sites providing health-related content, as it can impact their credibility and ranking in health-related searches.
 - Example: A higher healthScore indicates better quality and reliability of health content.

### clutterScore:
 - Description: Delta site-level signal in Q* penalizing sites with a large number of distracting/annoying resources loaded by the site.
 - Importance: This score helps in identifying and penalizing sites with poor user experience due to clutter, which can affect user engagement and rankings.
 - Example: A lower clutterScore indicates a cleaner, more user-friendly site.

### nsrOverrideBid:
 - Description: This signal is used to unconditionally override NSR as a bid in Q*. Should only be used in case of emergency.
 - Importance: This parameter allows for emergency adjustments to the NSR score, which can be critical in maintaining site performance during unexpected issues.
 - Example: A value greater than 0.001 would activate the override.

### siteQualityStddev:
 - Description: Estimate of site's PQ rating stddev--spread of the page-level PQ ratings of a site.
 - Importance: This score indicates the consistency of page quality across the site, which can influence overall site quality perception.
 - Example: A lower siteQualityStddev suggests more consistent page quality across the site.

## GoogleApi.ContentWarehouse.V1.Model.WWWDocInfo

### isRoboted:
 - Description: Indicates if the document is disallowed for crawling according to the host's robots.txt.
 - Importance: Ensuring that important pages are not disallowed for crawling can improve their visibility in search engine results.
 - Example: `isRoboted: false`

### seenNoindex:
 - Description: Indicates if the document has a noindex meta robots flag.
 - Importance: Pages with a noindex flag will not appear in search engine results, so it's crucial to ensure that important pages do not have this flag.
 - Example: `seenNoindex: false`

### seenNoarchive:
 - Description: Indicates if the document has a noarchive meta robots flag.
 - Importance: Pages with a noarchive flag will not be cached by search engines, which can affect their availability in search results.
 - Example: `seenNoarchive: false`

### seenNosnippet:
 - Description: Indicates if the document has a nosnippet meta robots flag.
 - Importance: Pages with a nosnippet flag will not have a snippet shown in search results, which can reduce their click-through rate.
 - Example: `seenNosnippet: false`

### seenNotranslate:
 - Description: Indicates if the document has a notranslate meta robots flag.
 - Importance: Pages with a notranslate flag will not be offered for translation in search results, which can affect their accessibility to non-native speakers.
 - Example: `seenNotranslate: false`

### title:
 - Description: The landing page title.
 - Importance: The title tag is a critical on-page SEO element that helps search engines understand the content of the page and influences click-through rates.
 - Example: `title: "Best Practices for SEO"`

### metaDescriptionLanguages:
 - Description: Detected languages of the meta description if different from the document language.
 - Importance: Ensuring the meta description is in the same language as the document can improve relevance and user experience.
 - Example: `metaDescriptionLanguages: ["en"]`

### languageTag:
 - Description: The most probable language for the document.
 - Importance: Correct language tagging helps search engines serve the content to the appropriate audience.
 - Example: `languageTag: "en"`

### url:
 - Description: The URL of the document.
 - Importance: A well-structured URL can improve search engine crawling and user experience.
 - Example: `url: "[https://example.com/best-practices-seo](https://example.com/best-practices-seo)"`

### urlAfterRedirects:
 - Description: The URL after any redirects.
 - Importance: Ensuring the final URL is optimized and relevant can improve search engine indexing and user experience.
 - Example: `urlAfterRedirects: "[https://example.com/best-practices-seo](https://example.com/best-practices-seo)"`

### referrerUrl:
 - Description: The URL of the referring document.
 - Importance: Understanding referral traffic can help in optimizing link-building strategies.
 - Example: `referrerUrl: "[https://example.com](https://example.com/)"`

### crawlTime:
 - Description: The last time the document was crawled.
 - Importance: Knowing the crawl time can help in understanding how frequently the content is being indexed by search engines.
 - Example: `crawlTime: "2023-10-01T12:00:00Z"`

### bodySize:
 - Description: The size of the document.
 - Importance: Large documents may take longer to load, affecting user experience and search engine rankings.
 - Example: `bodySize: 102400`

### imageLicenseInfo:
 - Description: Information about the image license, such as the license URL and how to acquire the license.
 - Importance: Properly licensed images can avoid legal issues and improve the credibility of the content.
 - Example: `imageLicenseInfo: { licenseUrl: "[https://example.com/license](https://example.com/license)", acquisitionInfo: "Contact [example@example.com](mailto:example@example.com)" }`

### imageHeight:
 - Description: The height of the image.
 - Importance: Ensuring images have appropriate dimensions can improve page load times and user experience.
 - Example: `imageHeight: 600`

### imageWidth:
 - Description: The width of the image.
 - Importance: Ensuring images have appropriate dimensions can improve page load times and user experience.
 - Example: `imageWidth: 800`

### imageSize:
 - Description: The size of the image in bytes.
 - Importance: Optimizing image size can improve page load times and user experience.
 - Example: `imageSize: 204800`

### visibleImage:
 - Description: Indicates if the coupled image was visible on the page.
 - Importance: Visible images can enhance user engagement and improve the relevance of the content.
 - Example: `visibleImage: true`

### lowQualityMetadescription:
 - Description: Indicates if the meta description is of low quality.
 - Importance: High-quality meta descriptions can improve click-through rates and search engine rankings.
 - Example: `lowQualityMetadescription: false`

### rootpageDuplicateMetadescription:
 - Description: Indicates if the meta description is duplicated on many other pages and this page is the root page of such pages.
 - Importance: Unique meta descriptions can improve search engine rankings and avoid content duplication issues.
 - Example: `rootpageDuplicateMetadescription: false`

### foreignMetadescription:
 - Description: Indicates if the meta description is in a different language than the page.
 - Importance: Ensuring the meta description matches the page language can improve relevance and user experience.
 - Example: `foreignMetadescription: false`

### badMetadescription:
 - Description: Indicates if the meta description is flagged as bad.
 - Importance: High-quality meta descriptions can improve click-through rates and search engine rankings.
 - Example: `badMetadescription: false`

### boilerplateMetadescription:
 - Description: Indicates if the meta description is boilerplate.
 - Importance: Unique meta descriptions can improve search engine rankings and avoid content duplication issues.
 - Example: `boilerplateMetadescription: false`

### partialBoilerplateMetadescription:
 - Description: Indicates if the meta description is partially boilerplate.
 - Importance: Unique meta descriptions can improve search engine rankings and avoid content duplication issues.
 - Example: `partialBoilerplateMetadescription: false`

### fuzzyMetadescription:
 - Description: Indicates if the meta description is fuzzy.
 - Importance: Clear and precise meta descriptions can improve click-through rates and search engine rankings.
 - Example: `fuzzyMetadescription: false`

### qualityWithoutAdjustment:
 - Description: The quality score of the document.
 - Importance: Higher quality scores can improve search engine rankings and visibility.
 - Example: `qualityWithoutAdjustment: 0.85`

### contentType:
 - Description: The content type of the document.
 - Importance: Correct content type helps search engines understand and index the content appropriately.
 - Example: `contentType: "text/html"`

### encoding:
 - Description: The encoding of the document.
 - Importance: Proper encoding ensures the content is displayed correctly to users and search engines.
 - Example: `encoding: "UTF-8"`

### language:
 - Description: The language of the document.
 - Importance: Correct language tagging helps search engines serve the content to the appropriate audience.
 - Example: `language: "en"`

### languageTag:
 - Description: The most probable language for the document.
 - Importance: Correct language tagging helps search engines serve the content to the appropriate audience.
 - Example: `languageTag: "en"`

### bodyTitleLanguages:
 - Description: Detected languages of the body title if different from the document language.
 - Importance: Ensuring the body title is in the same language as the document can improve relevance and user experience.
 - Example: `bodyTitleLanguages: ["en"]`

### nsrSitechunk:
 - Description: Sitechunk used by NSR, often equivalent to HOST_LEVEL_V3 sitechunk.
 - Importance: Proper sitechunking can improve search engine indexing and relevance.
 - Example: `nsrSitechunk: "HOST_LEVEL_V3"`

### subindex:
 - Description: Subindex id of the document, used for logging if a shard has documents from multiple indices.
 - Importance: Proper subindexing can improve search engine indexing and relevance.
 - Example: `subindex: 1`

### urlEncoding:
 - Description: The URL encoding.
 - Importance: Proper URL encoding ensures the URL is correctly interpreted by search engines and users.
 - Example: `urlEncoding: 1`

### coupledUrl:
 - Description: The URL of the coupled document (e.g., image).
 - Importance: Ensuring coupled URLs are correct can improve search engine indexing and relevance.
 - Example: `coupledUrl: "[https://example.com/image](https://example.com/image)"`

### coupledUrlEncoding:
 - Description: The encoding of the coupled URL.
 - Importance: Proper URL encoding ensures the coupled URL is correctly interpreted by search engines and users.
 - Example: `coupledUrlEncoding: 1`

### referrerUrl:
 - Description: The URL of the referring document.
 - Importance: Understanding referral traffic can help in optimizing link-building strategies.
 - Example: `referrerUrl: "[https://example.com](https://example.com/)"`

### urlAfterRedirects:
 - Description: The URL after any redirects.
 - Importance: Ensuring the final URL is optimized and relevant can improve search engine indexing and user experience.
 - Example: `urlAfterRedirects: "[https://example.com/best-practices-seo](https://example.com/best-practices-seo)"`

### indexingTs:
 - Description: The timestamp when the document is exported from indexing.
 - Importance: Knowing the indexing timestamp can help in understanding the recency of the content in search engine results.
 - Example: `indexingTs: "2023-10-01T12:00:00Z"`

### imagePublisher:
 - Description: The publisher of the image.
 - Importance: Proper attribution of image publishers can improve credibility and avoid legal issues.
 - Example: `imagePublisher: "Example Publisher"`

### imageLicenseInfo:
 - Description: Information about the image license, such as the license URL and how to acquire the license.
 - Importance: Properly licensed images can avoid legal issues and improve the credibility of the content.
 - Example: `imageLicenseInfo: { licenseUrl: "[https://example.com/license](https://example.com/license)", acquisitionInfo: "Contact [example@example.com](mailto:example@example.com)" }`

### imageHeight:
 - Description: The height of the image.
 - Importance: Ensuring images have appropriate dimensions can improve page load times and user experience.
 - Example: `imageHeight: 600`

### imageWidth:
 - Description: The width of the image.
 - Importance: Ensuring images have appropriate dimensions can improve page load times and user experience.
 - Example: `imageWidth: 800`

### imageSize:
 - Description: The size of the image in bytes.
 - Importance: Optimizing image size can improve page load times and user experience.
 - Example: `imageSize: 204800`

### visibleImage:
 - Description: Indicates if the coupled image was visible on the page.
 - Importance: Visible images can enhance user engagement and improve the relevance of the content.
 - Example: `visibleImage: true`

### lowQualityMetadescription:
 - Description: Indicates if the meta description is of low quality.
 - Importance: High-quality meta descriptions can improve click-through rates and search engine rankings.
 - Example: `lowQualityMetadescription: false`

### rootpageDuplicateMetadescription:
 - Description: Indicates if the meta description is duplicated on many other pages and this page is the root page of such pages.
 - Importance: Unique meta descriptions can improve search engine rankings and avoid content duplication issues.
 - Example: `rootpageDuplicateMetadescription: false`

### foreignMetadescription:
 - Description: Indicates if the meta description is in a different language than the page.
 - Importance: Ensuring the meta description matches the page language can improve relevance and user experience.
 - Example: `foreignMetadescription: false`

### badMetadescription:
 - Description: Indicates if the meta description is flagged as bad.
 - Importance: High-quality meta descriptions can improve click-through rates and search engine rankings.
 - Example: `badMetadescription: false`

### boilerplateMetadescription:
 - Description: Indicates if the meta description is boilerplate.
 - Importance: Unique meta descriptions can improve search engine rankings and avoid content duplication issues.
 - Example: `boilerplateMetadescription: false`

### partialBoilerplateMetadescription:
 - Description: Indicates if the meta description is partially boilerplate.
 - Importance: Unique meta descriptions can improve search engine rankings and avoid content duplication issues.
 - Example: `partialBoilerplateMetadescription: false`

### fuzzyMetadescription:
 - Description: Indicates if the meta description is fuzzy.
 - Importance: Clear and precise meta descriptions can improve click-through rates and search engine rankings.
 - Example: `fuzzyMetadescription: false`

### qualityWithoutAdjustment:
 - Description: The quality score of the document.
 - Importance: Higher quality scores can improve search engine rankings and visibility.
 - Example: `qualityWithoutAdjustment: 0.85`

### contentType:
 - Description: The content type of the document.
 - Importance: Correct content type helps search engines understand and index the content appropriately.
 - Example: `contentType: "text/html"`

### encoding:
 - Description: The encoding of the document.
 - Importance: Proper encoding ensures the content is displayed correctly to users and search engines.
 - Example: `encoding: "UTF-8"`

### language:
 - Description: The language of the document.
 - Importance: Correct language tagging helps search engines serve the content to the appropriate audience.
 - Example: `language: "en"`

### languageTag:
 - Description: The most probable language for the document.
 - Importance: Correct language tagging helps search engines serve the content to the appropriate audience.
 - Example: `languageTag: "en"`

### bodyTitleLanguages:
 - Description: Detected languages of the body title if different from the document language.
 - Importance: Ensuring the body title is in the same language as the document can improve relevance and user experience.
 - Example: `bodyTitleLanguages: ["en"]`

### nsrSitechunk:
 - Description: Sitechunk used by NSR, often equivalent to HOST_LEVEL_V3 sitechunk.
 - Importance: Proper sitechunking can improve search engine indexing and relevance.
 - Example: `nsrSitechunk: "HOST_LEVEL_V3"`

### subindex:
 - Description: Subindex id of the document, used for logging if a shard has documents from multiple indices.
 - Importance: Proper subindexing can improve search engine indexing and relevance.
 - Example: `subindex: 1`

### urlEncoding:
 - Description: The URL encoding.
 - Importance: Proper URL encoding ensures the URL is correctly interpreted by search engines and users.
 - Example: `urlEncoding: 1`

### coupledUrl:
 - Description: The URL of the coupled document (e.g., image).
 - Importance: Ensuring coupled URLs are correct can improve search engine indexing and relevance.
 - Example: `coupledUrl: "[https://example.com/image](https://example.com/image)"`

### coupledUrlEncoding:
 - Description: The encoding of the coupled URL.
 - Importance: Proper URL encoding ensures the coupled URL is correctly interpreted by search engines and users.
 - Example: `coupledUrlEncoding: 1`

### referrerUrl:
 - Description: The URL of the referring document.
 - Importance: Understanding referral traffic can help in optimizing link-building strategies.
 - Example: `referrerUrl: "[https://example.com](https://example.com/)"`

### urlAfterRedirects:
 - Description: The URL after any redirects.
 - Importance: Ensuring the final URL is optimized and relevant can improve search engine indexing and user experience.
 - Example: `urlAfterRedirects: "[https://example.com/best-practices-seo](https://example.com/best-practices-seo)"`

### indexingTs:
 - Description: The timestamp when the document is exported from indexing.
 - Importance: Knowing the indexing timestamp can help in understanding the recency of the content in search engine results.
 - Example: `indexingTs: "2023-10-01T12:00:00Z"`

### imagePublisher:
 - Description: The publisher of the image.
 - Importance: Proper attribution of image publishers can improve credibility and avoid legal issues.
 - Example: `imagePublisher: "Example Publisher"`

### imageLicenseInfo:
 - Description: Information about the image license, such as the license URL and how to acquire the license.
 - Importance: Properly licensed images can avoid legal issues and improve the credibility of the content.
 - Example: `imageLicenseInfo: { licenseUrl: "[https://example.com/license](https://example.com/license)", acquisitionInfo: "Contact [example@example.com](mailto:example@example.com)" }`

### imageHeight:
 - Description: The height of the image.
 - Importance: Ensuring images have appropriate dimensions can improve page load times and user experience.
 - Example: `imageHeight: 600`

### imageWidth:
 - Description: The width of the image.
 - Importance: Ensuring images have appropriate dimensions can improve page load times and user experience.
 - Example: `imageWidth: 800`

### imageSize:
 - Description: The size of the image in bytes.
 - Importance: Optimizing image size can improve page load times and user experience.
 - Example: `imageSize: 204800`

### visibleImage:
 - Description: Indicates if the coupled image was visible on the page.
 - Importance: Visible images can enhance user engagement and improve the relevance of the content.
 - Example: `visibleImage: true`

### lowQualityMetadescription:
 - Description: Indicates if the meta description is of low quality.
 - Importance: High-quality meta descriptions can improve click-through rates and search engine rankings.
 - Example: `lowQualityMetadescription: false`

### rootpageDuplicateMetadescription:
 - Description: Indicates if the meta description is duplicated on many other pages and this page is the root page of such pages.
 - Importance: Unique meta descriptions can improve search engine rankings and avoid content duplication issues.
 - Example: `rootpageDuplicateMetadescription: false`

### foreignMetadescription:
 - Description: Indicates if the meta description is in a different language than the page.
 - Importance: Ensuring the meta description matches the page language can improve relevance and user experience.
 - Example: `foreignMetadescription: false`

### badMetadescription:
 - Description: Indicates if the meta description is flagged as bad.
 - Importance: High-quality meta descriptions can improve click-through rates and search engine rankings.
 - Example: `badMetadescription: false`

### boilerplateMetadescription:
 - Description: Indicates if the meta description is boilerplate.
 - Importance: Unique meta descriptions can improve search engine rankings and avoid content duplication issues.
 - Example: `boilerplateMetadescription: false`

### partialBoilerplateMetadescription:
 - Description: Indicates if the meta description is partially boilerplate.
 - Importance: Unique meta descriptions can improve search engine rankings and avoid content duplication issues.
 - Example: `partialBoilerplateMetadescription: false`

### fuzzyMetadescription:
 - Description: Indicates if the meta description is fuzzy.
 - Importance: Clear and precise meta descriptions can improve click-through rates and search engine rankings.
 - Example: `fuzzyMetadescription: false`

### qualityWithoutAdjustment:
 - Description: The quality score of the document.
 - Importance: Higher quality scores can improve search engine rankings and visibility.
 - Example: `qualityWithoutAdjustment: 0.85`

### contentType:
 - Description: The content type of the document.
 - Importance: Correct content type helps search engines understand and index the content appropriately.
 - Example: `contentType: "text/html"`

### encoding:
 - Description: The encoding of the document.
 - Importance: Proper encoding ensures the content is displayed correctly to users and search engines.
 - Example: `encoding: "UTF-8"`

### language:
 - Description: The language of the document.
 - Importance: Correct language tagging helps search engines serve the content to the appropriate audience.
 - Example: `language

## GoogleApi.ContentWarehouse.V1.Model.AnchorsAnchor

### creationDate:
 - Description: Used for history - the first and last time we have seen this anchor. This field records the time when a retweet is created.
 - Importance: Important for tracking the freshness and historical presence of an anchor, which can influence the perceived relevance and timeliness of the content.
 - Example: `creationDate: 1622548800` (Unix timestamp)

### origText:
 - Description: Original text, including capitalization and punctuation. Runs of whitespace are collapsed into a single space.
 - Importance: Preserves the exact original text of the anchor, which is crucial for accurate text analysis and relevance scoring.
 - Example: `origText: "This is the original text."`

### context2:
 - Description: This is a hash of terms near the anchor. (This is a second-generation hash replacing the value stored in the 'context' field.)
 - Importance: Provides context for the anchor, which helps in understanding the surrounding content and improving relevance.
 - Example: `context2: 123456789`

### fragment:
 - Description: The URL fragment for this anchor (the foo in [http://www.google.com#foo](http://www.google.com/#foo)).
 - Importance: Identifies specific sections within a page, which can be useful for deep linking and improving user navigation.
 - Example: `fragment: "section1"`

### sourceType:
 - Description: Records the quality of the anchor's source page and is correlated with but not identical to the index tier of the source page.
 - Importance: Indicates the quality of the source page, which can affect the anchor's weight in search rankings.
 - Example: `sourceType: 1` (TYPE_HIGH_QUALITY)

### pagerankWeight:
 - Description: Weight to be stored in linkmaps for pageranker.
 - Importance: Influences the PageRank calculation, which is a key factor in determining the importance and ranking of a page.
 - Example: `pagerankWeight: 0.8`

### isLocal:
 - Description: Indicates whether an anchor's source and target pages are on the same domain.
 - Importance: Helps in determining the relationship between pages, which can affect internal linking strategies and SEO.
 - Example: `isLocal: true`

### originalTargetDocid:
 - Description: The docid of the anchor's original target. This field is available if and only if the anchor is forwarded.
 - Importance: Tracks the original target of the anchor, which is important for understanding link redirections and canonicalization.
 - Example: `originalTargetDocid: "doc12345"`

### fullLeftContext:
 - Description: The full context. These are not written out in the linklogs.
 - Importance: Provides additional context for the anchor, which can improve the understanding of its relevance.
 - Example: `fullLeftContext: ["previous", "words", "in", "context"]`

### linkTags:
 - Description: Contains info on link type, source page, etc.
 - Importance: Provides metadata about the link, which can be used for categorization and filtering.
 - Example: `linkTags: [1, 2, 3]`

### forwardingTypes:
 - Description: How the anchor is forwarded to the canonical, available only for forwarded anchors.
 - Importance: Helps in understanding the redirection and canonicalization process, which is important for SEO.
 - Example: `forwardingTypes: 2`

### locality:
 - Description: For ranking purposes, the quality of an anchor is measured by its "locality" and "bucket".
 - Importance: Affects the ranking of the anchor based on its locality, which can influence search results.
 - Example: `locality: 1`

### text:
 - Description: Space-delimited anchor words. Text that needs segmentation (like CJK or Thai) is unsegmented.
 - Importance: Represents the anchor text, which is a critical factor in link relevance and SEO.
 - Example: `text: "anchor words"`

### targetUrlEncoding:
 - Description: Stores the URL encoding with each source anchor to find the encoding most likely to be expected by the Web site.
 - Importance: Ensures the correct encoding of URLs, which is important for accurate link resolution and user experience.
 - Example: `targetUrlEncoding: 1`

### firstseenDate:
 - Description: Days past Dec 31, 1994, 23:00:00 UTC (Unix time @788914800) that this link was first seen.
 - Importance: Tracks when the link was first seen, which can be used for historical analysis and freshness scoring.
 - Example: `firstseenDate: 10000`

### lastUpdateTimestamp:
 - Description: The timestamp this anchor is updated in indexing.
 - Importance: Tracks the last update time, which is important for maintaining the freshness and accuracy of the index.
 - Example: `lastUpdateTimestamp: 1622548800`

### offset:
 - Description: The offset for the first term in the anchor - it can be used as a unique ID for the anchor within the document.
 - Importance: Helps in identifying and ordering anchors within a document, which is important for link analysis.
 - Example: `offset: 256`

### weight:
 - Description: Weights are 0-127.
 - Importance: Determines the importance of the anchor, which can influence its impact on search rankings.
 - Example: `weight: 50`

### encodedNewsAnchorData:
 - Description: Encoded data containing information about newsiness of anchor. Populated only if anchor is classified as coming from a newsy, high quality site.
 - Importance: Indicates the newsworthiness of the anchor, which can affect its relevance and ranking in news-related searches.
 - Example: `encodedNewsAnchorData: 123456`

### compressedImageUrls:
 - Description: If the anchor contained images, these image URLs are stored here in compressed form.
 - Importance: Stores image URLs associated with the anchor, which can be useful for image search and content analysis.
 - Example: `compressedImageUrls: ["[http://example.com/image1.jpg](http://example.com/image1.jpg)", "[http://example.com/image2.jpg](http://example.com/image2.jpg)"]`

## GoogleApi.ContentWarehouse.V1.Model.Anchors

### anchor
 - Description: A list of anchor objects of type `GoogleApi.ContentWarehouse.V1.Model.AnchorsAnchor.t`.
 - Importance: Anchors are crucial for understanding the linking structure of a website. They help in determining the relevance and authority of a page based on the links pointing to it.
 - Example: `[GoogleApi.ContentWarehouse.V1.Model.AnchorsAnchor.t()]`

### homepageAnchorsDropped
 - Description: The total number of local homepage anchors dropped in AnchorAccumulator.
 - Importance: This parameter indicates how many homepage anchors were not considered during the crawling process. Understanding this can help webmasters optimize their homepage links to ensure they are not being dropped.
 - Example: `"5"`

### indexTier
 - Description: The index tier from which the anchors were extracted. This is only valid in the anchor record written by linkextractor.
 - Importance: Knowing the index tier can help webmasters understand the priority and importance of the extracted anchors, which can influence how they structure their internal linking.
 - Example: `2`

### localAnchorsDropped
 - Description: The total number of local non-homepage anchors dropped in AnchorAccumulator.
 - Importance: This parameter shows how many local (non-homepage) anchors were dropped, which can help webmasters identify and fix issues with internal linking on subpages.
 - Example: `"10"`

### nonlocalAnchorsDropped
 - Description: The total number of non-local anchors dropped in AnchorAccumulator.
 - Importance: This parameter indicates how many external anchors were dropped, which can help webmasters understand the effectiveness of their external linking strategy.
 - Example: `"3"`

### redundantAnchorsDropped
 - Description: The total number of redundant anchors dropped in linkextractor.
 - Importance: Identifying redundant anchors can help webmasters clean up unnecessary links, improving the overall link structure and potentially enhancing SEO.
 - Example: `"7"`

### targetDocid
 - Description: The document ID of the target.
 - Importance: Knowing the target document ID can help in tracking and analyzing specific documents within the content warehouse, aiding in better content management and optimization.
 - Example: `"123456"`

### targetSite
 - Description: HOST_LEVEL site chunking.
 - Importance: This parameter helps in understanding how the site is chunked at the host level, which can influence how content is organized and served.
 - Example: `"example.com"`

### targetUrl
 - Description: The URL of the target, produced during link extraction but not written out in the linklogs to save space.
 - Importance: Knowing the target URL is essential for tracking the destination of links, which can help in analyzing link performance and optimizing link structures.
 - Example: `"[https://example.com/page](https://example.com/page)"`




## GoogleApi.ContentWarehouse.V1.Model.PerDocData

### uacSpamScore:
 - Description: The uac spam score is represented in 7 bits, going from 0 to 127. Threshold is 64. Score >= 64 is considered as uac spam.
 - Importance: This parameter helps in identifying and filtering out spam content, which is crucial for maintaining the quality of search results.
 - Example: uacSpamScore: 70

### spamtokensContentScore:
 - Description: For SpamTokens content scores. Used in SiteBoostTwiddler to determine whether a page is UGC Spam.
 - Importance: This score is used to identify user-generated content (UGC) spam, which can negatively impact the user experience if not filtered out.
 - Example: spamtokensContentScore: 0.85

### webrefEntities:
 - Description: WebRef entities associated to the document.
 - Importance: Associating WebRef entities helps in understanding the context and relevance of the document, improving search result accuracy.
 - Example: webrefEntities: {entity_id: "12345", entity_name: "Example Entity"}

### lastSignificantUpdate:
 - Description: Last significant update of the document. This is sourced from the quality_timebased.LastSignificantUpdate proto as computed by the LSUSelector from various signals. The value is a UNIX timestamp in seconds.
 - Importance: Knowing the last significant update helps in determining the freshness of the content, which is a key factor in search ranking.
 - Example: lastSignificantUpdate: "1625097600"

### homepagePagerankNs:
 - Description: The page-rank of the homepage of the site. Copied from the cdoc.doc().pagerank_ns() of the homepage.
 - Importance: Homepage PageRank is an indicator of the overall authority and trustworthiness of the site, influencing the ranking of its pages.
 - Example: homepagePagerankNs: 8

### numUrls:
 - Description: Total number of urls encoded in the url section = # of alternate urls + 1.
 - Importance: The number of URLs can indicate the breadth of content and interlinking within the site, affecting crawl efficiency and indexing.
 - Example: numUrls: 5

### datesInfo:
 - Description: Stores dates-related info (e.g. page is old based on its date annotations). Used in FreshnessTwiddler.
 - Importance: Date-related information is crucial for assessing the relevance and timeliness of the content.
 - Example: datesInfo: "2021-07-01"

### semanticDate:
 - Description: SemanticDate, estimated date of the content of a document based on the contents of the document (via parsing), anchors and related documents. Date is encoded as a 32-bits UNIX date (1970 Jan 1 epoch).
 - Importance: Semantic dates help in understanding the temporal context of the content, which can be important for time-sensitive queries.
 - Example: semanticDate: 1625097600

### semanticDateInfo:
 - Description: Info is encoded using a SemanticDate specific format. Contains confidence scores for day/month/year components as well as various meta data required by the freshness twiddlers.
 - Importance: Provides detailed temporal metadata that can be used to fine-tune the freshness and relevance of search results.
 - Example: semanticDateInfo: 123456

### toolbarPagerank:
 - Description: A copy of the value stored in /namespace/indexing/wwwglobal//fakepr/* for this document. A value between 0 and 10 (inclusive) means that this is the toolbar pagerank of the page.
 - Importance: Toolbar PageRank is a simplified measure of a page's importance and can influence its ranking in search results.
 - Example: toolbarPagerank: 5

### freshnessEncodedSignals:
 - Description: Stores freshness and aging related data, such as time-related quality metrics predicted from url-pattern level signals.
 - Importance: Freshness signals are used to determine how up-to-date the content is, which is important for ranking in time-sensitive searches.
 - Example: freshnessEncodedSignals: "encoded_freshness_data"

### originalTitleHardTokenCount:
 - Description: The number of hard tokens in the title.
 - Importance: The number of hard tokens in the title can affect the document's relevance to specific queries.
 - Example: originalTitleHardTokenCount: 5

### rosettaLanguages:
 - Description: Top two document language BCP-47 codes as generated by the RosettaLanguageAnnotator in the decreasing order of probability.
 - Importance: Language identification is crucial for serving the document to the appropriate audience and improving search result relevance.
 - Example: rosettaLanguages: ["en", "es"]

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages).
 - Importance: Identifying the language of video content helps in serving it to the right audience and improving user experience.
 - Example: videoLanguage: {language_code: "en"}

### watchpageLanguageResult:
 - Description: Language classified by the WatchPageLanguage Model. Only present for watch pages.
 - Importance: Accurate language classification ensures that video content is correctly indexed and served to users.
 - Example: watchpageLanguageResult: {language_code: "en"}

### videoCorpusDocid:
 - Description: Unique identifier for video documents in the corpus.
 - Importance: Ensures that video content is uniquely identifiable and retrievable in the search index.
 - Example: videoCorpusDocid: "video12345"

### videoLanguage:
 - Description: Audio-based language classified by Automatic Language Identification (only for watch pages