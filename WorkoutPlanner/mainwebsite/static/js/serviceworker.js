// Versioned cache name to manage updates. 
// Change this string whenever you update the files being cached, to force the browser to re-cache.
const cacheName = 'myfirstwebsite-pwa-v1';

// List of URLs to cache during installation.
// These should match actual served URLs (routes and static file paths).
const assetsToCache = [
    '/',                             // Homepage (Django route for views.index)
    '/contact/',                     // Contact page (views.contact)
    '/dashboard/',                    // Test page (views.testpage)
    '/signup/',                    // Student listing (views.student_list_view)

    // Static assets (adjust paths as needed)
    '/static/css/styles.css',        // CSS file used globally
    '/static/css/index.css',         // Page-specific CSS
    '/static/images/angry.png',  // App icon for Android or general use
    '/static/images/alien.png',  // Larger app icon
    '/static/images/logo.png',       // App/website logo

    // Offline fallback page
    '/static/offline.html'           // Simple page served when user is offline and no cache match is found
];

// Install event: Occurs when the service worker is installed.
// This is where we cache all necessary assets upfront.
self.addEventListener('install', event => {
    event.waitUntil(
        // Open a cache with the specified name
        caches.open(cacheName).then(cache => {
            // Add all defined assets to that cache
            return cache.addAll(assetsToCache);
        })
    );
});

// Activate event: Optional cleanup step when activating a new version of the service worker.
// This helps remove old cache versions to save storage space.
self.addEventListener('activate', event => {
    event.waitUntil(
        // Get all existing cache keys
        caches.keys().then(keys => {
            // Filter out the current cache and delete any older versions
            return Promise.all(
                keys.filter(key => key !== cacheName)
                    .map(key => caches.delete(key))
            );
        })
    );
});

// Fetch event: Intercepts every request the page makes (HTML, CSS, JS, images, etc.)
self.addEventListener('fetch', event => {
    // Try to serve from cache first
    event.respondWith(
        caches.match(event.request).then(cachedResponse => {
            if (cachedResponse) {
                // Return cached file if found
                return cachedResponse;
            }

            // If not in cache, try to fetch it from the network
            return fetch(event.request).catch(() => {
                // If both fail (e.g., user is offline), serve the offline fallback
                if (event.request.mode === 'navigate') {
                    // Only show offline.html for page navigations (not images, CSS, etc.)
                    return caches.match('/static/offline.html');
                }
            });
        })
    );
});
