import { OpenPanel } from '@openpanel/web';

// Single shared instance — import `op` wherever you need to track events
export const op = new OpenPanel({
   clientId: import.meta.env.VITE_OPENPANEL_CLIENT_ID,
   apiUrl: import.meta.env.VITE_OPENPANEL_API_URL,
   clientSecret: import.meta.env.VITE_OPENPANEL_CLIENT_SECRET,
   trackScreenViews: true, // auto-tracks route changes
   trackOutgoingLinks: true, // auto-tracks clicks to external URLs
   trackAttributes: true, // enables data-track="event_name" on HTML elements
});
