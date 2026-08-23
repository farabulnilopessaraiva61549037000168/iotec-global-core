;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="c9c53287-259f-a1cb-0cfe-4d11c37a4ba6")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,561646,e=>{"use strict";var t=e.i(730497);e.s(["usePricingFlags",0,function(){return{"flag-cheaper-core":(0,t.useFlag)({controlName:"flag-cheaper-core",default:!1}),"flag-revised-plans-q1-2026":(0,t.useFlag)({controlName:"flag-revised-plans-q1-2026",default:!1})}}])},972152,e=>{"use strict";let t="razorpay";e.s(["CHECKOUT_PAYMENT_PROVIDER_RAZORPAY",0,t,"COUNTRY_PROVIDER_MAP",0,{IN:t}])},229375,e=>{"use strict";var t=e.i(420180),n=e.i(568087),o=e.i(596139),r=e.i(561646);e.s(["usePlanCheckoutUrl",0,function(e){let a=(0,t.useRouter)(),s=function(e,t){if(e.prefix===o.corePlanPrefix){let n=(0,o.getCheckoutablePriceOption)({...e,flags:t});if(!n)throw Error(`Core price not found for interval ${e.interval}`);return`stripe-checkout-by-price/${n.externalId}`}let n=(0,o.getCheckoutablePriceOption)({...e,flags:t});if(!n)throw Error(`Pro price not found for interval ${e.interval}, tier ${e.tier}`);return`stripe-checkout-by-price/${n.externalId}`}(e,(0,r.usePricingFlags)()),i=a.query[n.BONSAI_VERSION_QUERY_PARAM],c=Array.isArray(i)?i[0]:i;return function({path:e,coupon:t,source:o,successRedirectPath:r,cancelRedirectPath:a,vBonsai:s}){let i=new URLSearchParams;t&&i.set("coupon",t),o&&i.set("source",o),r&&i.set("successRedirectPath",r),a&&i.set("cancelRedirectPath",a),s&&i.set(n.BONSAI_VERSION_QUERY_PARAM,s);let c=i.toString();return`/${e}${c?`?${c}`:""}`}({path:s,source:e.source,coupon:e.coupon,successRedirectPath:e.successRedirectPath,cancelRedirectPath:e.cancelRedirectPath,vBonsai:c})}],229375)},982728,e=>{"use strict";function t(){if(document.getElementById("razorpay-color-scheme-fix"))return;let e=document.createElement("style");e.id="razorpay-color-scheme-fix",e.textContent='iframe[src*="razorpay"] { color-scheme: light; }\n#rzp-sdk-root, .rzp-sdk-root { color-scheme: light; }',document.head.appendChild(e)}let n=new Map;function o(e){let t=n.get(e);if(t)return t;document.querySelector(`script[src="${e}"]`)?.remove();let o=new Promise((t,o)=>{let r=document.createElement("script");r.src=e,r.onload=()=>{n.delete(e),t()},r.onerror=()=>{n.delete(e),o(Error(`Failed to load script: ${e}`))},document.head.appendChild(r)});return n.set(e,o),o}async function r(){t(),window.RZPCrossBorderPrePay||(await o("https://checkout.razorpay.com/v1/checkout.js"),await o("https://cross-border-cdn.razorpay.com/custom-pre-payment-module/build/browser/rzp-xb-pre-pay-module.min.js"))}e.s(["MERCHANT_IMAGE",0,"https://replit.com/public/images/replit-logo.png","MERCHANT_NAME",0,"Replit","MERCHANT_THEME",0,{color:"#232430"},"injectRazorpayColorSchemeFix",0,t,"loadRazorpayScript",0,r,"loadScript",0,o])},326523,e=>{"use strict";var t=e.i(389959),n=e.i(973245),o=e.i(304277);e.i(566901);let r={},a=n.gql`
    query RegionalPaymentProviderCountry {
  country
}
    `;function s(e){let t={...r,...e};return o.useQuery(a,t)}var i=e.i(972152),c=e.i(730497),l=e.i(776065);e.s(["useRegionalPaymentProvider",0,function(){let e=(0,c.useFlag)({controlName:"flag-razorpay-checkout",default:!1}),n=(0,l.useQueryParam)("payment_region","string"),{data:o,refetch:r}=s({skip:!e}),a=(0,t.useRef)(null);if((0,t.useEffect)(()=>{e&&a.current!==n&&(a.current=n,r())},[e,n,r]),!e)return null;let u=o?.country??"",d=i.COUNTRY_PROVIDER_MAP[u]??null;return null===d?null:d},"useUserCountry",0,function(){let{data:e}=s();return e?.country??null}],326523)},911261,e=>{"use strict";var t=e.i(972152),n=e.i(420180),o=e.i(389959),r=e.i(973245),a=e.i(951262);let s={},i=r.gql`
    mutation ConfirmRazorpayCheckout($input: ConfirmRazorpayCheckoutInput!) {
  confirmRazorpayCheckout(input: $input)
}
    `,c=r.gql`
    mutation CreateReplitPlanCheckoutSessionForRazorpay($input: CreateReplitPlanCheckoutSessionInput!) {
  createReplitPlanCheckoutSession(input: $input) {
    ... on RazorpayCheckoutSessionResult {
      checkoutToken
      keyId
      checkoutSessionId
      currency
      prefillName
      prefillEmail
      amount
    }
    ... on UserError {
      message
    }
    ... on UnauthorizedError {
      message
    }
    ... on TooManyRequestsError {
      message
    }
  }
}
    `;var l=e.i(320216),u=e.i(982728),d=e.i(326523);e.s(["useRegionalCheckout",0,function({onSuccess:e,onBeforeOpen:r,onDismiss:p}={}){let C=(0,d.useRegionalPaymentProvider)(),{openCheckout:m,isLoading:g}=function({onSuccess:e,onBeforeOpen:t,onDismiss:r}={}){let d,p,[C,m]=(0,o.useState)(!1),{showError:g}=(0,l.default)(),y=(0,n.useRouter)(),[h]=(d={...s,...void 0},a.useMutation(c,d)),[f]=(p={...s,...void 0},a.useMutation(i,p));return{openCheckout:(0,o.useCallback)(async({planPrefix:n,planPeriod:o,promoCodeExternalId:a,priceExternalId:s})=>{m(!0);let i=!1;try{let{data:c}=await h({variables:{input:{planPrefix:n,planPeriod:o,promoCodeExternalId:a,priceExternalId:s}}}),l=c?.createReplitPlanCheckoutSession;if(l?.__typename!=="RazorpayCheckoutSessionResult"||!l.keyId||!l.checkoutToken||null==l.amount||!l.currency)return void g("Unable to start checkout. Please try again.");if(await (0,u.loadRazorpayScript)(),!window.RZPCrossBorderPrePay)return void g("Unable to load payment provider. Please try again.");t&&(t(),i=!0,await new Promise(e=>setTimeout(e,250))),new window.RZPCrossBorderPrePay({key:l.keyId,amount:l.amount,currency:l.currency,name:u.MERCHANT_NAME,image:u.MERCHANT_IMAGE,theme:u.MERCHANT_THEME,checkout_session_id:l.checkoutToken,prefill:{name:l.prefillName??void 0,email:l.prefillEmail??void 0}},{onPaymentEvent:t=>{if("payment.success"!==t.event)return;let n=t.payment,o=t.razorpay_payment_id??n?.razorpay_payment_id;o&&l.checkoutSessionId&&f({variables:{input:{checkoutSessionId:l.checkoutSessionId,razorpayPaymentId:o}}}).catch(()=>{}),e?.(),y.push(`/stripe-checkout-success?sessionId=${l.checkoutSessionId}`)},onError:()=>{g("Payment failed. Please try again."),r?.()},onDismiss:()=>{r?.()}}).open()}catch{g("Checkout failed. Please try again."),i&&r?.()}finally{m(!1)}},[f,h,t,r,e,y,g]),isLoading:C}}({onSuccess:e,onBeforeOpen:r,onDismiss:p});return C===t.CHECKOUT_PAYMENT_PROVIDER_RAZORPAY?{openCheckout:m,isLoading:g,provider:C}:{openCheckout:null,isLoading:!1,provider:C}}],911261)},481963,e=>{"use strict";var t=e.i(973245);let n=t.gql`
    fragment TrialWillCancelAtCurrentUser on CurrentUser {
  id
  isSubscribed
  paymentMethod {
    __typename
    ... on PaymentMethod {
      id
      isSaved
    }
  }
  billingInfo {
    planInfo {
      cancelAt
    }
  }
  userSubscription {
    isTrial
    timeRemainingInTrial
  }
}
    `,o=t.gql`
    fragment UserPlanStateCurrentUser on CurrentUser {
  id
  ...TrialWillCancelAtCurrentUser
  userSubscriptionType
  billingInfo {
    planInfo {
      interval
      provider
    }
  }
  userSubscription {
    isTrial
  }
}
    ${n}`;e.s(["TrialWillCancelAtCurrentUserFragmentDoc",0,n,"UserPlanStateCurrentUserFragmentDoc",0,o])},843036,e=>{"use strict";var t=e.i(973245),n=e.i(481963),o=e.i(304277);e.i(566901);let r={},a=t.gql`
    query UpgradeButton {
  currentUser {
    id
    ...UserPlanStateCurrentUser
  }
}
    ${n.UserPlanStateCurrentUserFragmentDoc}`;e.s(["useUpgradeButtonQuery",0,function(e){let t={...r,...e};return o.useQuery(a,t)}])},532563,810461,e=>{"use strict";var t=e.i(908796),n=e.i(596139);let o=e=>"month"===e?"monthly":"year"===e?"yearly":null;e.s(["planPeriodFromInterval",0,o],810461);let r=e=>{let{billingInfo:t,userSubscription:n,paymentMethod:o}=e,r=o?.__typename==="PaymentMethod"&&o.isSaved;if(!n?.isTrial)return null;let a=t?.planInfo?.cancelAt??(r?null:n?.timeRemainingInTrial??null);return a?new Date(a):null};e.s(["getCurrentPlanState",0,function({user:e}){let{userSubscriptionType:a,billingInfo:s,userSubscription:i}=e;if(null==i||null==a)return{showUpgradeCta:!0,plan:{name:n.freePlanName}};let c=r(e),l=a===t.UserSubscriptionTypeEnum.Pro?n.proPlanName:n.corePlanName,u=!1===i.isTrial,d=!0===i.isTrial&&null===c;return{showUpgradeCta:!u&&!d,plan:{name:l,period:o(s?.planInfo?.interval),trial:i?.isTrial?{cancelsAt:c,isManuallyCancelled:(e=>{let{billingInfo:t}=e;return!!t?.planInfo?.cancelAt})(e)}:null,provider:s?.planInfo?.provider??t.PaymentProviderEnum.Stripe}}},"trialWillCancelAt",0,r],532563)},3466,e=>{"use strict";var t,n=e.i(276385),o=e.i(843036),r=e.i(712903),a=e.i(596139),s=e.i(229375),i=e.i(532563),c=e.i(415541),l=e.i(709485),u=e.i(911261),d=e.i(242917),p=e.i(643484),C=e.i(419635),m=e.i(488299),g=((t=g||{}).TrialUpgrade="trial_upgrade",t.Default="default",t);e.s(["default",0,({context:e,variant:t="outlined",onCancel:g,onClickCallback:y,text:h,surface:f,onPlanCheckoutComplete:S,iconButton:R,redirectPath:E,modalHeadingText:P,modalSubHeadingText:A,directCheckout:O=!1,planPeriod:I="monthly",..._})=>{let{loading:b}=(()=>{let{data:e,loading:t}=(0,o.useUpgradeButtonQuery)();if(t)return{loading:!0,upgradeType:null};let n=e?.currentUser?(0,i.getCurrentPlanState)({user:e.currentUser}):null;return n?.plan.name===a.corePlanName&&null!==n.plan.trial?{loading:!1,upgradeType:"trial_upgrade"}:{loading:!1,upgradeType:"default"}})(),{show:N}=(0,d.useGlobalModal)(),{openCheckout:T,isLoading:v}=(0,u.useRegionalCheckout)(),x=(0,s.usePlanCheckoutUrl)({prefix:a.corePlanPrefix,interval:I,source:e,successRedirectPath:E,cancelRedirectPath:E}),k=h||`Join Replit ${a.corePlanName}`,U=()=>{(0,c.track)(l.events.UPGRADE_SELECTED,{source:e}),y&&y()},w=async()=>{U();try{await N("MembershipPurchaseModal",{analyticsContext:{upgrade:{context:e,surface:f}},onPurchaseComplete:S,redirectPath:E,headingText:P,subHeadingText:A})}finally{g&&g()}};if(R)return(0,n.jsx)(m.IconButton,{alt:k,onClick:w,disabled:b,children:(0,n.jsx)(r.default,{})});if(O){let{hideCoreIcon:e,className:o,clsx:s,disabled:i,slot:c,...l}=_;if(T){let e=b||v;return(0,n.jsx)(p.Button,{...l,iconLeft:_.hideCoreIcon?void 0:(0,n.jsx)(r.default,{}),variant:t,clsx:[o,s,{loading:e,loaded:!e}],disabled:e||i,loading:e,onClick:()=>{U(),T({planPrefix:a.corePlanPrefix,planPeriod:I})},text:k})}return(0,n.jsx)(C.ButtonLink,{...l,iconLeft:_.hideCoreIcon?void 0:(0,n.jsx)(r.default,{}),variant:t,clsx:[o,s,{loading:b,loaded:!b}],disabled:b||i,href:x,onClick:U,text:k})}return(0,n.jsx)(p.Button,{..._,iconLeft:_.hideCoreIcon?void 0:(0,n.jsx)(r.default,{}),variant:t,clsx:[_.className,_.clsx,{loading:b,loaded:!b}],loading:b,onClick:w,text:k})}])},595996,e=>{"use strict";var t=e.i(276385),n=e.i(389959),o=e.i(983420),r=e.i(967629),a=e.i(919073),s=e.i(691636),i=e.i(61732),c=e.i(727223);let l=(0,r.css)([s.rcss.overflow("hidden"),s.rcss.position.relative]),u={16:4,20:4,24:4,32:4,36:4,48:4,64:8,84:16};function d(e){let r=(0,n.useContext)(o.IconContext),{size:d=r.size??32,alt:p=r.alt??"",iconUrl:C}=e,m=d<32?4:8;function g(){return(0,t.jsx)(i.View,{css:{position:"absolute",top:0,left:0,width:"100%",height:"100%",boxShadow:"inset 0px 0px 0px 1px #80808040",borderRadius:m}})}if(C.endsWith(".svg")){let e=u[d],n=d-2*e;return(0,t.jsxs)(a.ShadesSurface,{css:[s.rcss.p(e),s.rcss.borderRadius(m),l,s.rcss.width(d),s.rcss.height(d)],children:[(0,t.jsx)(i.View,{css:[s.rcss.position.relative,s.rcss.width(n),s.rcss.height(n)],children:(0,t.jsx)(c.default,{alt:p,src:C,objectFit:"contain",layout:"fill"})}),(0,t.jsx)(g,{})]})}return(0,t.jsxs)(a.ShadesSurface,{css:[l,s.rcss.borderRadius(m),s.rcss.width(d),s.rcss.height(d)],children:[(0,t.jsx)(c.default,{alt:p,src:C,width:d,height:d,objectFit:"cover"}),(0,t.jsx)(g,{})]})}e.s(["ReplIconWithPlaceholder",0,function({isLoading:e,alt:n,iconUrl:o,size:r=32}){let i=o&&void 0!==n?(0,t.jsx)(d,{alt:n,iconUrl:o,size:r}):null;if(!e&&i)return i;let c=r<32?4:8;return(0,t.jsx)(a.ShadesSurface,{css:[l,s.rcss.borderRadius(c),s.rcss.width(r),s.rcss.height(r)]})},"default",0,d])},335451,366541,e=>{"use strict";var t=e.i(973245),n=e.i(304277);e.i(566901);let o={},r=t.gql`
    fragment ConnectorContextReplInfo on Repl {
  id
  title
  iconUrl
  url
  timeCreated
  user {
    id
    username
    fullName
    image
  }
}
    `,a=t.gql`
    fragment ConnectorContextConnectionInfo on OintConnection {
  connectionId
  connectorName
  displayName
  iconPath
  status
  type
  environment
  webhookProvider
  repls {
    ...ConnectorContextReplInfo
  }
  predefinedProvider {
    id
    displayName
    description
    baseUrl
    iconPath
  }
}
    ${r}`,s=t.gql`
    fragment ConnectorContext on CurrentUserConnectorContext {
  openIntClientToken
  connectorWhitelist
  connections {
    ...ConnectorContextConnectionInfo
  }
  connectorConfigs {
    id
    type
    connectorName
    displayName
    description
    iconPath
    webhookEvents {
      name
      model
      description
    }
  }
}
    ${a}`,i=t.gql`
    fragment OrgConnectorContext on OrgConnectorContext {
  openIntClientToken
  connectorWhitelist
  connections {
    ...ConnectorContextConnectionInfo
  }
  connectorConfigs {
    id
    type
    connectorName
    displayName
    description
    iconPath
    webhookEvents {
      name
      model
      description
    }
  }
}
    ${a}`,c=t.gql`
    query GetConnectorContext {
  currentUser {
    ... on CurrentUser {
      id
      isSubscribed
      connectorContext {
        ...ConnectorContext
      }
    }
  }
}
    ${s}`,l=t.gql`
    query GetConnectorContextByOrg($orgId: String!) {
  currentUser {
    ... on CurrentUser {
      id
      isSubscribed
      org(orgId: $orgId) {
        __typename
        ... on Org {
          id
          connectorContext {
            ...OrgConnectorContext
          }
        }
        ... on Error {
          __typename
          message
        }
      }
    }
  }
}
    ${i}`;e.s(["ConnectorContextConnectionInfoFragmentDoc",0,a,"ConnectorContextFragmentDoc",0,s,"ConnectorContextReplInfoFragmentDoc",0,r,"GetConnectorContextByOrgDocument",0,l,"GetConnectorContextDocument",0,c,"OrgConnectorContextFragmentDoc",0,i,"useGetConnectorContextByOrgQuery",0,function(e){let t={...o,...e};return n.useQuery(l,t)},"useGetConnectorContextQuery",0,function(e){let t={...o,...e};return n.useQuery(c,t)}],366541);var u=e.i(951262);let d={},p=t.gql`
    query UserConnectorsPage {
  currentUser {
    id
    __typename
    isSubscribed
    connectorContext {
      __typename
      ...ConnectorContext
      ... on Error {
        message
      }
    }
  }
}
    ${s}`,C=t.gql`
    mutation CreateConnection($input: CreateConnectionInput!) {
  createConnection(input: $input) {
    ... on CreateConnection {
      connectionId
    }
    ... on Error {
      message
    }
  }
}
    `,m=t.gql`
    mutation DeleteConnection($input: DeleteConnectionInput!) {
  deleteConnection(input: $input) {
    ... on DeleteConnection {
      success
    }
  }
}
    `,g=t.gql`
    mutation RequestNewConnector($input: RequestNewConnectorInput!) {
  requestNewConnector(input: $input) {
    ... on RequestNewConnectorResult {
      success
    }
  }
}
    `;e.s(["UserConnectorsPageDocument",0,p,"useCreateConnectionMutation",0,function(e){let t={...d,...e};return u.useMutation(C,t)},"useDeleteConnectionMutation",0,function(e){let t={...d,...e};return u.useMutation(m,t)},"useRequestNewConnectorMutation",0,function(e){let t={...d,...e};return u.useMutation(g,t)},"useUserConnectorsPageQuery",0,function(e){let t={...d,...e};return n.useQuery(p,t)}],335451)},829706,e=>{"use strict";var t=e.i(276385),n=e.i(917736),o=e.i(882848),r=e.i(995691),a=e.i(146432),s=e.i(480028);let i=new Set(["FIGMA","CUSTOM_MCP"]),c=new Set(["BITBUCKET_SOURCE_CONTROL","GITHUB_SOURCE_CONTROL","GITLAB_SOURCE_CONTROL"]),l=new Set(["STRIPE"]),u=new Set(["disconnected","error"]),d=new Set(["YOUTUBE"]),p=[{id:"replit-database",name:"Replit Database",type:"PostgreSQL",icon:(0,t.jsx)(n.default,{size:16,color:s.tokens.blueStronger}),link:"https://docs.replit.com/cloud-services/storage-and-databases/sql-database",pane:{type:"neon"}},{id:"replit-app-storage",name:"Replit App Storage",type:"Object Storage",icon:(0,t.jsx)(a.default,{size:16,color:s.tokens.greenStronger}),link:"https://docs.replit.com/cloud-services/storage-and-databases/object-storage",pane:{type:"objectStorage"}},{id:"replit-auth",name:"Replit Auth",type:"Authentication",icon:(0,t.jsx)(r.default,{size:16,color:s.tokens.orangeStronger}),link:"https://docs.replit.com/replit-workspace/replit-auth#replit-auth",pane:{type:"replitAuth"}},{id:"replit-domains",name:"Replit Domains",type:"Domains",icon:(0,t.jsx)(o.default,{size:16,color:s.tokens.tealStronger}),link:"https://docs.replit.com/cloud-services/deployments/domain-purchasing",pane:{type:"deployments"}}];e.s(["APP_SCOPED_CONNECTORS",0,l,"CONNECTOR_DESCRIPTIONS",0,{AGENTMAIL:"Send, receive, and reply to emails using the AgentMail email inbox API.",AMPLITUDE:"Query analytics data, manage event taxonomy, and trigger project runs in Amplitude",ASHBY:"Access job postings, candidates, and applications from your Ashby ATS",ASANA:"Read tasks and project data from Asana workspaces",SPROUTSOCIAL:"Manage social media profiles, posts, messages, and cases from Sprout Social",BITBUCKET:"Access Bitbucket repositories, users, and organizations from Replit",BITBUCKET_SOURCE_CONTROL:"Sync code to Bitbucket repositories from your Replit apps",GITHUB_SOURCE_CONTROL:"Sync code to GitHub repositories from your Replit apps",GITLAB_SOURCE_CONTROL:"Sync code to GitLab projects from your Replit apps",DATABRICKS_M2M:"Execute SQL queries and manage data workflows in Databricks using a service account",BIGQUERY:"Execute SQL queries on Google BigQuery datasets from your Replit apps",BOX:"Access Box files and folders from Replit",CALENDLY:"View Calendly events and event types",CONFLUENCE:"Read users and groups, create and edit content in Confluence spaces",CLICKUP:"Access tasks, projects, and workflows in ClickUp",DATABRICKS:"Execute SQL queries and manage data workflows in Databricks",DISCORD:"Access Discord guild information and user profiles",DROPBOX:"Access Dropbox files, content, and metadata",ELEVENLABS:"AI voice generation and text-to-speech",HEX:"Run data notebooks, manage projects, and trigger Hex project runs via API",OPENAI:"Access your own OpenAI API key instead of default Replit-managed AI integrations",FACEBOOK:"View Facebook profiles, posts, photos, and manage pages",GITHUB:"Access GitHub repositories, users, and organizations from your Replit apps",GOOGLE_CALENDAR:"Read and write Google Calendar events and settings",GOOGLE_DOCS:"Create, read, and edit Google Docs",GOOGLE_DRIVE:"Access and manage Google Drive files and folders",GOOGLE_MAIL:"Send, receive, and manage Gmail messages",GOOGLE_SHEET:"Read and write data in Google Sheets",GOOGLE_SLIDES:"Create, read, and edit Google Slides presentations",HUBSPOT:"Access HubSpot CRM objects, contacts, and deals from Replit",INSTAGRAM:"Manage Instagram business content, messages, and insights",JIRA:"View users and manage Jira work items and issues",LINEAR:"Create and manage Linear issues, comments, and schedules",MONDAY:"Access Monday.com boards and user information",MOBILE_MAPS:"Access mobile maps and locations from Replit",NOTION:"Read and write to Notion workspaces and pages",ONEDRIVE:"Access and manage OneDrive files and folders",OUTLOOK:"Send and receive emails, manage Outlook calendar events",PLAID:"Access Plaid connected bank accounts and transactions",POSTGRES:"Execute read-only SQL queries on PostgreSQL databases",RESEND:"Send transactional emails using the Resend API",REVENUECAT:"Monetize your mobile apps built on Replit",SALESFORCE:"Access Salesforce CRM data and perform operations via REST API",SEGMENT:"Manage Segment sources, destinations, and tracking plans via the Public API",SENDGRID:"Send transactional emails using the SendGrid API",SHAREPOINT:"Read, write, and manage SharePoint sites and documents",SLACK:"Send messages and interact with Slack workspaces",SLACK_AGENT:"Integrate Slack agent capabilities from Replit",SLACK_AGENT_BUILDER:"Build and manage custom Slack agents",STRIPE:"Connect to Stripe to enable seamless and secure payments for your apps",SNOWFLAKE:"Execute SQL queries on Snowflake data warehouses",SPOTIFY:"Access and manage Spotify playlists and libraries",TODOIST:"Read and write to your Todoist tasks and projects",TWILIO:"Send SMS messages and make voice calls using the Twilio API",YOUTUBE:"Upload and manage YouTube videos, channels, and analytics",ZENDESK:"Access Zendesk users and support tickets from Replit",FIGMA:"Allow Replit Agent to view and rapidly build your designs from Figma",CUSTOM_MCP:"Allows Replit Agent to access external MCP servers",ZOOM:"Access Zoom meetings, users, settings, and webinars with admin privileges",WORKATO:"Trigger Workato recipes and call Workato APIs",X:"Access X posts, users, and search using the X API v2 with pay-per-usage pricing",MICROSOFT_FABRIC:"Access Microsoft Fabric workspaces and resources"},"DISCONNECTED_STATUSES",0,u,"MCP_CONNECTORS",0,i,"REPLIT_MANAGED_SERVICES",0,p,"VERSION_CONTROL_CONNECTORS",0,c,"buildConnectionManagementUrl",0,function(e,t){return`/integrations/${e.toLowerCase()}/apps/${t}`},"isAppScopedConnector",0,e=>l.has(e),"isConnectionHealthy",0,e=>!u.has(e??""),"isHiddenUnlessConnected",0,e=>d.has(e),"isMCPConnector",0,e=>i.has(e),"toConnectorName",0,function(e){if(!e)return null;let t=e.toUpperCase();return/^[A-Z][A-Z0-9_]*$/.test(t)?t:null}])},246549,e=>{"use strict";var t=e.i(389959),n=e.i(335451),o=e.i(366541),r=e.i(829706),a=e.i(151027);let s={};e.s(["useConnectors",0,function(e){let i=e?.skip??!1,{orgId:c}=(0,a.useCurrentUserStoredOrgContext)(),l=!!c,{data:u,loading:d,error:p,refetch:C}=(0,o.useGetConnectorContextQuery)({skip:i||l,context:s}),{data:m,loading:g,error:y,refetch:h}=(0,o.useGetConnectorContextByOrgQuery)({variables:{orgId:c??""},skip:i||!l,context:s}),f=u?.currentUser?.__typename==="CurrentUser"?u?.currentUser?.connectorContext:null,S=m?.currentUser?.__typename==="CurrentUser"&&m?.currentUser?.org?.__typename==="Org"?m?.currentUser?.org?.connectorContext:null,R=l?S:f,E=l?y:p,P=l?g:d,A=l?h:C,[O,{loading:I}]=(0,n.useCreateConnectionMutation)(),_=(0,t.useCallback)(async e=>O({...e,refetchQueries:l?[{query:o.GetConnectorContextByOrgDocument,variables:{orgId:c??""}}]:[{query:o.GetConnectorContextDocument}]}),[O,l,c]),b=R&&(l?"OrgConnectorContext"===R.__typename:"CurrentUserConnectorContext"===R.__typename),N=l?m?.currentUser?.__typename==="CurrentUser"&&m.currentUser.isSubscribed:u?.currentUser?.__typename==="CurrentUser"&&u.currentUser.isSubscribed,T=(0,t.useMemo)(()=>{if(!b||"CurrentUserConnectorContext"!==R.__typename&&"OrgConnectorContext"!==R.__typename)return[];let e=[],t=R.connectorWhitelist??[],n=R.connections??[],o=R.connectorConfigs??[],a=n.filter(e=>(t.includes(e.connectorName)||r.MCP_CONNECTORS.has(e.connectorName))&&!r.APP_SCOPED_CONNECTORS.has(e.connectorName)),s=new Set(a.map(e=>e.connectorName)),i=new Map;o.forEach(e=>{e.connectorName&&e.webhookEvents&&e.webhookEvents.length>0&&i.set(e.connectorName,e.webhookEvents)});let c=o.filter(e=>e.connectorName&&t.includes(e.connectorName)&&!s.has(e.connectorName)&&"CUSTOM_MCP"!==e.connectorName);return a.forEach(t=>{e.push({id:t.connectionId,displayName:t.displayName,iconPath:t.iconPath,connectorName:t.connectorName,connectorType:"connection",type:t.type,webhookEvents:i.get(t.connectorName)})}),c.forEach(t=>{t.connectorName&&e.push({id:t.id,displayName:t.displayName??"Untitled",iconPath:t.iconPath,connectorName:t.connectorName,connectorType:"connectorConfig",type:t.type,webhookEvents:i.get(t.connectorName)})}),e},[b,R]);return E||!b||"CurrentUserConnectorContext"!==R.__typename&&"OrgConnectorContext"!==R.__typename?{token:null,connections:[],connectorConfigs:[],connectorWhitelist:[],slashCommandConnectorItems:[],createConnection:_,loading:P,createConnectionLoading:I,error:E,refetch:A,isSubscribed:N??!1,isOrgContext:l}:{token:R.openIntClientToken,connections:R.connections??[],connectorConfigs:R.connectorConfigs??[],connectorWhitelist:R.connectorWhitelist??[],slashCommandConnectorItems:T,createConnection:_,loading:P,createConnectionLoading:I,error:E,refetch:A,isSubscribed:N??!1,isOrgContext:l}}])},843400,e=>{e.v({modalContent:"EmbedModal-module__oAShma__modalContent",overlay:"EmbedModal-module__oAShma__overlay",overlayTopAligned:"EmbedModal-module__oAShma__overlayTopAligned"})},554370,e=>{"use strict";var t=e.i(276385),n=e.i(389959),o=e.i(486597),r=e.i(624071),a=e.i(342942),s=e.i(739261),i=e.i(969407),c=e.i(918542),l=e.i(691636),u=e.i(61732),d=e.i(843400);e.s(["EmbedModal",0,function({isOpen:e,onRequestClose:p,children:C,maxWidth:m=800,maxHeight:g,centered:y=!0,zIndex:h,className:f,portalContainer:S}){let R=(0,i.useIsSSR)(),E=(0,n.useRef)(null),P=(0,o.useOverlayTriggerState)({isOpen:e,onOpenChange:e=>{e||p()}}),{modalProps:A,underlayProps:O}=(0,c.useModalOverlay)({isDismissable:!0,isKeyboardDismissDisabled:!1,shouldCloseOnInteractOutside:e=>!(e.tagName.toLowerCase().includes("1password")||e.tagName.toLowerCase().includes("com-1password")||e.hasAttribute("data-op-target")||e.hasAttribute("data-op-id")||Array.from(e.attributes).some(e=>e.name.startsWith("data-1p-"))||e.className?.toString().includes("op-")||null!==e.closest('[class*="1password"]')||null!==e.closest('[class*="op-"]')||null!==e.closest("[data-op-target]"))},P,E),{dialogProps:I}=(0,s.useDialog)({"aria-label":"Embed content"},E);return((0,n.useEffect)(()=>{let t=t=>{"Escape"===t.key&&e&&p()};return document.addEventListener("keydown",t),()=>document.removeEventListener("keydown",t)},[e,p]),R||!e)?null:(0,t.jsx)(a.Overlay,{portalContainer:S??document.body,children:(0,t.jsx)("div",{...O,className:y?d.default.overlay:`${d.default.overlay} ${d.default.overlayTopAligned}`,style:{zIndex:h??l.DefaultModalZIndex},children:(0,t.jsx)("div",{...(0,r.mergeProps)(A,I),ref:E,className:`${d.default.modalContent} ${f||""}`,style:{maxWidth:m,maxHeight:g??"calc(100vh - 64px)"},children:(0,t.jsx)(u.View,{children:C})})})})}])}]);

//# debugId=c9c53287-259f-a1cb-0cfe-4d11c37a4ba6
//# sourceMappingURL=0kj5weylv7-75.js.map
