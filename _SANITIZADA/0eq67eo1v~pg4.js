;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="e82d1463-55e4-ea43-b731-d2df83f11738")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,335451,366541,e=>{"use strict";var t=e.i(973245),n=e.i(304277);e.i(566901);let r={},o=t.gql`
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
    `,s=t.gql`
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
    ${o}`,a=t.gql`
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
    ${s}`,i=t.gql`
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
    ${s}`,l=t.gql`
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
    ${a}`,c=t.gql`
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
    ${i}`;e.s(["ConnectorContextConnectionInfoFragmentDoc",0,s,"ConnectorContextFragmentDoc",0,a,"ConnectorContextReplInfoFragmentDoc",0,o,"GetConnectorContextByOrgDocument",0,c,"GetConnectorContextDocument",0,l,"OrgConnectorContextFragmentDoc",0,i,"useGetConnectorContextByOrgQuery",0,function(e){let t={...r,...e};return n.useQuery(c,t)},"useGetConnectorContextQuery",0,function(e){let t={...r,...e};return n.useQuery(l,t)}],366541);var u=e.i(951262);let d={},p=t.gql`
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
    ${a}`,g=t.gql`
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
    `,C=t.gql`
    mutation RequestNewConnector($input: RequestNewConnectorInput!) {
  requestNewConnector(input: $input) {
    ... on RequestNewConnectorResult {
      success
    }
  }
}
    `;e.s(["UserConnectorsPageDocument",0,p,"useCreateConnectionMutation",0,function(e){let t={...d,...e};return u.useMutation(g,t)},"useDeleteConnectionMutation",0,function(e){let t={...d,...e};return u.useMutation(m,t)},"useRequestNewConnectorMutation",0,function(e){let t={...d,...e};return u.useMutation(C,t)},"useUserConnectorsPageQuery",0,function(e){let t={...d,...e};return n.useQuery(p,t)}],335451)},829706,e=>{"use strict";var t=e.i(276385),n=e.i(917736),r=e.i(882848),o=e.i(995691),s=e.i(146432),a=e.i(480028);let i=new Set(["FIGMA","CUSTOM_MCP"]),l=new Set(["BITBUCKET_SOURCE_CONTROL","GITHUB_SOURCE_CONTROL","GITLAB_SOURCE_CONTROL"]),c=new Set(["STRIPE"]),u=new Set(["disconnected","error"]),d=new Set(["YOUTUBE"]),p=[{id:"replit-database",name:"Replit Database",type:"PostgreSQL",icon:(0,t.jsx)(n.default,{size:16,color:a.tokens.blueStronger}),link:"https://docs.replit.com/cloud-services/storage-and-databases/sql-database",pane:{type:"neon"}},{id:"replit-app-storage",name:"Replit App Storage",type:"Object Storage",icon:(0,t.jsx)(s.default,{size:16,color:a.tokens.greenStronger}),link:"https://docs.replit.com/cloud-services/storage-and-databases/object-storage",pane:{type:"objectStorage"}},{id:"replit-auth",name:"Replit Auth",type:"Authentication",icon:(0,t.jsx)(o.default,{size:16,color:a.tokens.orangeStronger}),link:"https://docs.replit.com/replit-workspace/replit-auth#replit-auth",pane:{type:"replitAuth"}},{id:"replit-domains",name:"Replit Domains",type:"Domains",icon:(0,t.jsx)(r.default,{size:16,color:a.tokens.tealStronger}),link:"https://docs.replit.com/cloud-services/deployments/domain-purchasing",pane:{type:"deployments"}}];e.s(["APP_SCOPED_CONNECTORS",0,c,"CONNECTOR_DESCRIPTIONS",0,{AGENTMAIL:"Send, receive, and reply to emails using the AgentMail email inbox API.",AMPLITUDE:"Query analytics data, manage event taxonomy, and trigger project runs in Amplitude",ASHBY:"Access job postings, candidates, and applications from your Ashby ATS",ASANA:"Read tasks and project data from Asana workspaces",SPROUTSOCIAL:"Manage social media profiles, posts, messages, and cases from Sprout Social",BITBUCKET:"Access Bitbucket repositories, users, and organizations from Replit",BITBUCKET_SOURCE_CONTROL:"Sync code to Bitbucket repositories from your Replit apps",GITHUB_SOURCE_CONTROL:"Sync code to GitHub repositories from your Replit apps",GITLAB_SOURCE_CONTROL:"Sync code to GitLab projects from your Replit apps",DATABRICKS_M2M:"Execute SQL queries and manage data workflows in Databricks using a service account",BIGQUERY:"Execute SQL queries on Google BigQuery datasets from your Replit apps",BOX:"Access Box files and folders from Replit",CALENDLY:"View Calendly events and event types",CONFLUENCE:"Read users and groups, create and edit content in Confluence spaces",CLICKUP:"Access tasks, projects, and workflows in ClickUp",DATABRICKS:"Execute SQL queries and manage data workflows in Databricks",DISCORD:"Access Discord guild information and user profiles",DROPBOX:"Access Dropbox files, content, and metadata",ELEVENLABS:"AI voice generation and text-to-speech",HEX:"Run data notebooks, manage projects, and trigger Hex project runs via API",OPENAI:"Access your own OpenAI API key instead of default Replit-managed AI integrations",FACEBOOK:"View Facebook profiles, posts, photos, and manage pages",GITHUB:"Access GitHub repositories, users, and organizations from your Replit apps",GOOGLE_CALENDAR:"Read and write Google Calendar events and settings",GOOGLE_DOCS:"Create, read, and edit Google Docs",GOOGLE_DRIVE:"Access and manage Google Drive files and folders",GOOGLE_MAIL:"Send, receive, and manage Gmail messages",GOOGLE_SHEET:"Read and write data in Google Sheets",GOOGLE_SLIDES:"Create, read, and edit Google Slides presentations",HUBSPOT:"Access HubSpot CRM objects, contacts, and deals from Replit",INSTAGRAM:"Manage Instagram business content, messages, and insights",JIRA:"View users and manage Jira work items and issues",LINEAR:"Create and manage Linear issues, comments, and schedules",MONDAY:"Access Monday.com boards and user information",MOBILE_MAPS:"Access mobile maps and locations from Replit",NOTION:"Read and write to Notion workspaces and pages",ONEDRIVE:"Access and manage OneDrive files and folders",OUTLOOK:"Send and receive emails, manage Outlook calendar events",PLAID:"Access Plaid connected bank accounts and transactions",POSTGRES:"Execute read-only SQL queries on PostgreSQL databases",RESEND:"Send transactional emails using the Resend API",REVENUECAT:"Monetize your mobile apps built on Replit",SALESFORCE:"Access Salesforce CRM data and perform operations via REST API",SEGMENT:"Manage Segment sources, destinations, and tracking plans via the Public API",SENDGRID:"Send transactional emails using the SendGrid API",SHAREPOINT:"Read, write, and manage SharePoint sites and documents",SLACK:"Send messages and interact with Slack workspaces",SLACK_AGENT:"Integrate Slack agent capabilities from Replit",SLACK_AGENT_BUILDER:"Build and manage custom Slack agents",STRIPE:"Connect to Stripe to enable seamless and secure payments for your apps",SNOWFLAKE:"Execute SQL queries on Snowflake data warehouses",SPOTIFY:"Access and manage Spotify playlists and libraries",TODOIST:"Read and write to your Todoist tasks and projects",TWILIO:"Send SMS messages and make voice calls using the Twilio API",YOUTUBE:"Upload and manage YouTube videos, channels, and analytics",ZENDESK:"Access Zendesk users and support tickets from Replit",FIGMA:"Allow Replit Agent to view and rapidly build your designs from Figma",CUSTOM_MCP:"Allows Replit Agent to access external MCP servers",ZOOM:"Access Zoom meetings, users, settings, and webinars with admin privileges",WORKATO:"Trigger Workato recipes and call Workato APIs",X:"Access X posts, users, and search using the X API v2 with pay-per-usage pricing",MICROSOFT_FABRIC:"Access Microsoft Fabric workspaces and resources"},"DISCONNECTED_STATUSES",0,u,"MCP_CONNECTORS",0,i,"REPLIT_MANAGED_SERVICES",0,p,"VERSION_CONTROL_CONNECTORS",0,l,"buildConnectionManagementUrl",0,function(e,t){return`/integrations/${e.toLowerCase()}/apps/${t}`},"isAppScopedConnector",0,e=>c.has(e),"isConnectionHealthy",0,e=>!u.has(e??""),"isHiddenUnlessConnected",0,e=>d.has(e),"isMCPConnector",0,e=>i.has(e),"toConnectorName",0,function(e){if(!e)return null;let t=e.toUpperCase();return/^[A-Z][A-Z0-9_]*$/.test(t)?t:null}])},246549,e=>{"use strict";var t=e.i(389959),n=e.i(335451),r=e.i(366541),o=e.i(829706),s=e.i(151027);let a={};e.s(["useConnectors",0,function(e){let i=e?.skip??!1,{orgId:l}=(0,s.useCurrentUserStoredOrgContext)(),c=!!l,{data:u,loading:d,error:p,refetch:g}=(0,r.useGetConnectorContextQuery)({skip:i||c,context:a}),{data:m,loading:C,error:f,refetch:y}=(0,r.useGetConnectorContextByOrgQuery)({variables:{orgId:l??""},skip:i||!c,context:a}),h=u?.currentUser?.__typename==="CurrentUser"?u?.currentUser?.connectorContext:null,x=m?.currentUser?.__typename==="CurrentUser"&&m?.currentUser?.org?.__typename==="Org"?m?.currentUser?.org?.connectorContext:null,v=c?x:h,O=c?f:p,S=c?C:d,b=c?y:g,[I,{loading:E}]=(0,n.useCreateConnectionMutation)(),A=(0,t.useCallback)(async e=>I({...e,refetchQueries:c?[{query:r.GetConnectorContextByOrgDocument,variables:{orgId:l??""}}]:[{query:r.GetConnectorContextDocument}]}),[I,c,l]),_=v&&(c?"OrgConnectorContext"===v.__typename:"CurrentUserConnectorContext"===v.__typename),w=c?m?.currentUser?.__typename==="CurrentUser"&&m.currentUser.isSubscribed:u?.currentUser?.__typename==="CurrentUser"&&u.currentUser.isSubscribed,R=(0,t.useMemo)(()=>{if(!_||"CurrentUserConnectorContext"!==v.__typename&&"OrgConnectorContext"!==v.__typename)return[];let e=[],t=v.connectorWhitelist??[],n=v.connections??[],r=v.connectorConfigs??[],s=n.filter(e=>(t.includes(e.connectorName)||o.MCP_CONNECTORS.has(e.connectorName))&&!o.APP_SCOPED_CONNECTORS.has(e.connectorName)),a=new Set(s.map(e=>e.connectorName)),i=new Map;r.forEach(e=>{e.connectorName&&e.webhookEvents&&e.webhookEvents.length>0&&i.set(e.connectorName,e.webhookEvents)});let l=r.filter(e=>e.connectorName&&t.includes(e.connectorName)&&!a.has(e.connectorName)&&"CUSTOM_MCP"!==e.connectorName);return s.forEach(t=>{e.push({id:t.connectionId,displayName:t.displayName,iconPath:t.iconPath,connectorName:t.connectorName,connectorType:"connection",type:t.type,webhookEvents:i.get(t.connectorName)})}),l.forEach(t=>{t.connectorName&&e.push({id:t.id,displayName:t.displayName??"Untitled",iconPath:t.iconPath,connectorName:t.connectorName,connectorType:"connectorConfig",type:t.type,webhookEvents:i.get(t.connectorName)})}),e},[_,v]);return O||!_||"CurrentUserConnectorContext"!==v.__typename&&"OrgConnectorContext"!==v.__typename?{token:null,connections:[],connectorConfigs:[],connectorWhitelist:[],slashCommandConnectorItems:[],createConnection:A,loading:S,createConnectionLoading:E,error:O,refetch:b,isSubscribed:w??!1,isOrgContext:c}:{token:v.openIntClientToken,connections:v.connections??[],connectorConfigs:v.connectorConfigs??[],connectorWhitelist:v.connectorWhitelist??[],slashCommandConnectorItems:R,createConnection:A,loading:S,createConnectionLoading:E,error:O,refetch:b,isSubscribed:w??!1,isOrgContext:c}}])},843400,e=>{e.v({modalContent:"EmbedModal-module__oAShma__modalContent",overlay:"EmbedModal-module__oAShma__overlay",overlayTopAligned:"EmbedModal-module__oAShma__overlayTopAligned"})},554370,e=>{"use strict";var t=e.i(276385),n=e.i(389959),r=e.i(486597),o=e.i(624071),s=e.i(342942),a=e.i(739261),i=e.i(969407),l=e.i(918542),c=e.i(691636),u=e.i(61732),d=e.i(843400);e.s(["EmbedModal",0,function({isOpen:e,onRequestClose:p,children:g,maxWidth:m=800,maxHeight:C,centered:f=!0,zIndex:y,className:h,portalContainer:x}){let v=(0,i.useIsSSR)(),O=(0,n.useRef)(null),S=(0,r.useOverlayTriggerState)({isOpen:e,onOpenChange:e=>{e||p()}}),{modalProps:b,underlayProps:I}=(0,l.useModalOverlay)({isDismissable:!0,isKeyboardDismissDisabled:!1,shouldCloseOnInteractOutside:e=>!(e.tagName.toLowerCase().includes("1password")||e.tagName.toLowerCase().includes("com-1password")||e.hasAttribute("data-op-target")||e.hasAttribute("data-op-id")||Array.from(e.attributes).some(e=>e.name.startsWith("data-1p-"))||e.className?.toString().includes("op-")||null!==e.closest('[class*="1password"]')||null!==e.closest('[class*="op-"]')||null!==e.closest("[data-op-target]"))},S,O),{dialogProps:E}=(0,a.useDialog)({"aria-label":"Embed content"},O);return((0,n.useEffect)(()=>{let t=t=>{"Escape"===t.key&&e&&p()};return document.addEventListener("keydown",t),()=>document.removeEventListener("keydown",t)},[e,p]),v||!e)?null:(0,t.jsx)(s.Overlay,{portalContainer:x??document.body,children:(0,t.jsx)("div",{...I,className:f?d.default.overlay:`${d.default.overlay} ${d.default.overlayTopAligned}`,style:{zIndex:y??c.DefaultModalZIndex},children:(0,t.jsx)("div",{...(0,o.mergeProps)(b,E),ref:O,className:`${d.default.modalContent} ${h||""}`,style:{maxWidth:m,maxHeight:C??"calc(100vh - 64px)"},children:(0,t.jsx)(u.View,{children:g})})})})}])},283063,e=>{e.v({divider:"DividerH-module__AtpSyW__divider"})},903790,e=>{"use strict";var t=e.i(276385),n=e.i(283063);e.s(["DividerH",0,function({className:e,style:r}){return(0,t.jsx)("div",{clsx:[n.default.divider,e],style:r})}])},151027,873054,672220,284693,e=>{"use strict";var t=e.i(276385),n=e.i(420180),r=e.i(389959),o=e.i(973245);let s=o.gql`
    fragment OrgFlagsOrg on Org {
  id
  flags {
    id
    type
    value
  }
}
    `;e.s(["OrgFlagsOrgFragmentDoc",0,s],873054);var a=e.i(304277);e.i(566901);var i=e.i(951262);let l={},c=o.gql`
    fragment CurrentUserOrg on Org {
  id
  slug
  currentUserRole
  dealContext {
    dealType
    salesContactEmail
  }
  ...OrgFlagsOrg
}
    ${s}`,u=o.gql`
    query CurrentUserOrgContext {
  getUserOrgContext2 {
    ... on Org {
      ...CurrentUserOrg
    }
  }
}
    ${c}`;function d(e){let t={...l,...e};return a.useQuery(u,t)}let p=o.gql`
    query CurrentUserOrgContextGetOrg($orgSlug: String!) {
  currentUser {
    id
    org(orgSlug: $orgSlug) {
      ... on Org {
        id
        ...CurrentUserOrg
      }
      ... on Error {
        message
      }
    }
  }
}
    ${c}`;function g(e){let t={...l,...e};return a.useQuery(p,t)}let m=o.gql`
    mutation CurrentUserOrgContextUpdateOrgContext($input: UpdateOrgContextInput!) {
  updateOrgContext(input: $input) {
    ... on Org {
      ...CurrentUserOrg
    }
    ... on Error {
      __typename
      message
    }
  }
}
    ${c}`;e.s(["CurrentUserOrgContextDocument",0,u,"CurrentUserOrgContextUpdateOrgContextDocument",0,m,"useCurrentUserOrgContextGetOrgQuery",0,g,"useCurrentUserOrgContextQuery",0,d,"useCurrentUserOrgContextUpdateOrgContextMutation",0,function(e){let t={...l,...e};return i.useMutation(m,t)}],672220),e.i(908796);let C={"flag-sponsorship-bulk-send":"number","flag-org-depl-rules":"boolean","flag-require-git-remote":"boolean","flag-agent-billing-v2-teams":"boolean","flag-org-stack-templates":"boolean","flag-tom-riddle":"boolean","flag-deployments-switch-to-azure":"boolean","flag-experimental-connectors":"string","flag-org-require-security-scan-in-deployment":"boolean","flag-enable-deployment-private-passwords":"boolean","flag-org-custom-mcp-servers":"boolean","flag-org-predefined-mcp-providers":"boolean","flag-org-budgets":"boolean","flag-azure-org-can-use-object-store":"boolean","flag-unified-plans-enterprise":"boolean","flag-self-hosted-git-domains":"boolean","flag-databricks-apps":"boolean","flag-enterprise-deployment-geography-whitelist":"boolean","flag-deployment-geography-selection":"boolean"};function f(e){if(!e||"object"!=typeof e)return!1;let{id:t,type:n,value:r}=e;if(!(t in C))return!1;let o=C[t];return n===o||"number"===o&&"string"===n&&!isNaN(Number(r))}function y(e){return(e.flags||[]).filter(f).reduce((e,{id:t,value:n})=>({...e,[t]:"number"===C[t]?Number(n):n}),{})}e.s(["orgFlags",0,y],284693);var h=e.i(933302);let x=["/evaluations","/import","/integrations","/notifications","/templates","/theme","/@","/~/cli","/grab"],v=(0,r.createContext)(null),O=(0,r.createContext)(null);function S(){let e=(0,r.useContext)(v);if(null===e)throw Error("StoredOrgContextProvider missing!");return e}e.s(["StoredOrgContextProvider",0,function({children:e}){let o=(0,n.useRouter)(),s=o.asPath,a=function(){let e=(0,n.useRouter)().asPath.split("?")[0];if(e.startsWith("/t")){let t=e.split("/");if(t[2])return t[2]}return null}(),i=(0,h.useSyncStatsigOrgContext)(),l=null!=a,c=!l&&x.some(e=>s.startsWith(e)),u=d({skip:"/replEnvironmentDesktop"===o.pathname||"/replEnvironmentMobile"===o.pathname||!c}),p=u.data?.getUserOrgContext2?.__typename==="Org"?u.data.getUserOrgContext2:null,m=g({skip:!l,variables:{orgSlug:a??""}}),C=m.data?.currentUser?.org?.__typename==="Org"?m.data.currentUser.org:null,f=c?u.loading:m.loading,S=l?C:c?p:null;i(S?.id,S?.dealContext?.dealType);let[b,I]=(0,r.useState)({orgId:S?.id,orgSlug:S?.slug,orgRole:S?.currentUserRole??void 0,orgDealContext:S?.dealContext??void 0});(0,r.useEffect)(()=>{f||I({orgId:S?.id,orgSlug:S?.slug,orgRole:S?.currentUserRole??void 0,orgDealContext:S?.dealContext??void 0})},[S,f]);let E=(0,r.useCallback)(e=>I(e),[]),A=(0,r.useMemo)(()=>S?y(S):{},[S]);return(0,t.jsx)(O.Provider,{value:E,children:(0,t.jsx)(v.Provider,{value:{flags:A,orgId:b.orgId,orgSlug:b.orgSlug,orgRole:b.orgRole,orgDealContext:b.orgDealContext,loading:f},children:e})})},"getOrgTrackingContext",0,e=>e?`Org:${e.id}`:"Personal","useCurrentUserStoredOrgContext",0,S,"useIsCurrentOrgEnterprise",0,function(){let e=S();return e.orgDealContext?.dealType==="enterprise"||e.orgDealContext?.dealType==="enterprise_trial"},"useSetOptimisticOrg",0,function(){let e=(0,r.useContext)(O);if(null===e)throw Error("StoredOrgContextProvider missing!");return e}],151027)},790281,e=>{e.v({background:"Switch-module__C40utW__background",button:"Switch-module__C40utW__button",label:"Switch-module__C40utW__label",svg:"Switch-module__C40utW__svg"})},327391,e=>{"use strict";e.i(142273);var t=e.i(276385),n=e.i(389959),r=e.i(497953),o=e.i(99906),s=e.i(138715),a=e.i(104394),i=e.i(330666),l=e.i(480028),c=e.i(8047),u=e.i(61732),d=e.i(790281);let p=u.SpecializedView.label;e.s(["Switch",0,({colorway:e="primary",dataCy:u,size:g="default",fillColor:m,focusRingColor:C,...f})=>{let y=l.colormap[e],h=(0,n.useRef)(null),x=(0,r.useToggleState)(f),{inputProps:v}=function(e,t,n){let{labelProps:r,inputProps:o,isSelected:s,isPressed:i,isDisabled:l,isReadOnly:c}=(0,a.useToggle)(e,t,n);return{labelProps:r,inputProps:{...o,role:"switch",checked:s},isSelected:s,isPressed:i,isDisabled:l,isReadOnly:c}}(f,x,h),{focusProps:O,isFocusVisible:S}=(0,o.useFocusRing)(f),{hoverProps:b,isHovered:I}=(0,s.useHover)(f),{isSelected:E}=x,A=f.isDisabled||!1,_=f.isReadOnly||!1,w=n.Children.count(f.children)>0;void 0!==f["aria-label"]||f["aria-labelledby"];let R="small"===g,N=R?26:38,T=R?16:24,U=R?8:12,k=R?12:16,P=N-1,D=T-1,L=N+2,M=T+2,G=U+1,j=(0,t.jsxs)("svg",{"aria-hidden":"true",...b,width:N,height:T,viewBox:`0 0 ${N} ${T}`,fill:"none",xmlns:"http://www.w3.org/2000/svg",overflow:S?"visible":"hidden",style:{cursor:A||_?"auto":"pointer",opacity:A?.4:1},className:d.default.svg,children:[(0,t.jsx)("rect",{x:"0",y:"0",width:N,height:T,rx:U,fill:m??(E?A||_?y.dimmer:y.default:l.tokens.interactiveBorder),className:d.default.background}),(0,t.jsx)("rect",{x:E?R?12:18:R?2:4,y:R?2:4,width:k,height:k,rx:R?6:8,fill:l.tokens.white,className:d.default.button}),(0,t.jsx)("rect",{x:"0.5",y:"0.5",width:P,height:D,rx:U,stroke:!I||A||_?"transparent":E?y.strongest:l.tokens.interactiveBorderHover,"data-switch-outline":!0}),(0,t.jsx)("rect",{x:"-1",y:"-1",stroke:S?C??(E?y.strongest:y.default):"transparent",width:L,height:M,rx:G,strokeWidth:"2"})]});return w?(0,t.jsxs)(p,{clsx:d.default.label,"data-cy":u,children:[(0,t.jsx)(i.VisuallyHidden,{children:(0,t.jsx)("input",{...v,...O,ref:h})}),j,(0,t.jsx)(c.Text,{multiline:!1,variant:R?"small":"text",children:f.children})]}):(0,t.jsxs)(p,{clsx:d.default.label,"data-cy":u,children:[(0,t.jsx)(i.VisuallyHidden,{children:(0,t.jsx)("input",{...v,...O,ref:h})}),j]})}],327391)},190545,e=>{"use strict";var t=e.i(276385),n=e.i(389959),r=e.i(593583),o=e.i(379778);let s=(0,n.forwardRef)(function({dataCy:e,...n},s){return(0,t.jsx)(r.Form,{...(0,o.useView)(n),ref:s,"data-cy":e})});e.s(["Form",0,s])},60337,e=>{e.v({decoratedInputInput:"Input-module__7pJrIG__decoratedInputInput",decoratedInputRoot:"Input-module__7pJrIG__decoratedInputRoot",input:"Input-module__7pJrIG__input",inputAutosize:"Input-module__7pJrIG__inputAutosize"})},528710,711486,e=>{"use strict";var t=e.i(276385),n=e.i(389959),r=e.i(964304),o=e.i(10425),s=e.i(983420),a=new Map;function i(e){var t=a.get(e);t&&t.destroy()}function l(e){var t=a.get(e);t&&t.update()}var c=null;"u"<typeof window?((c=function(e){return e}).destroy=function(e){return e},c.update=function(e){return e}):((c=function(e,t){return e&&Array.prototype.forEach.call(e.length?e:[e],function(e){return function(e){if(e&&e.nodeName&&"TEXTAREA"===e.nodeName&&!a.has(e)){var t,n=null,r=window.getComputedStyle(e),o=(t=e.value,function(){i({testForHeightReduction:""===t||!e.value.startsWith(t),restoreTextAlign:null}),t=e.value}),s=(function(t){e.removeEventListener("autosize:destroy",s),e.removeEventListener("autosize:update",l),e.removeEventListener("input",o),window.removeEventListener("resize",l),Object.keys(t).forEach(function(n){return e.style[n]=t[n]}),a.delete(e)}).bind(e,{height:e.style.height,resize:e.style.resize,textAlign:e.style.textAlign,overflowY:e.style.overflowY,overflowX:e.style.overflowX,wordWrap:e.style.wordWrap});e.addEventListener("autosize:destroy",s),e.addEventListener("autosize:update",l),e.addEventListener("input",o),window.addEventListener("resize",l),e.style.overflowX="hidden",e.style.wordWrap="break-word",a.set(e,{destroy:s,update:l}),l()}function i(t){var o,s,a=t.restoreTextAlign,l=void 0===a?null:a,c=t.testForHeightReduction,u=r.overflowY;if(0!==e.scrollHeight&&("vertical"===r.resize?e.style.resize="none":"both"===r.resize&&(e.style.resize="horizontal"),(void 0===c||c)&&(o=function(e){for(var t=[];e&&e.parentNode&&e.parentNode instanceof Element;)e.parentNode.scrollTop&&t.push([e.parentNode,e.parentNode.scrollTop]),e=e.parentNode;return function(){return t.forEach(function(e){var t=e[0],n=e[1];t.style.scrollBehavior="auto",t.scrollTop=n,t.style.scrollBehavior=null})}}(e),e.style.height=""),s="content-box"===r.boxSizing?e.scrollHeight-(parseFloat(r.paddingTop)+parseFloat(r.paddingBottom)):e.scrollHeight+parseFloat(r.borderTopWidth)+parseFloat(r.borderBottomWidth),"none"!==r.maxHeight&&s>parseFloat(r.maxHeight)?("hidden"===r.overflowY&&(e.style.overflow="scroll"),s=parseFloat(r.maxHeight)):"hidden"!==r.overflowY&&(e.style.overflow="hidden"),e.style.height=s+"px",l&&(e.style.textAlign=l),o&&o(),n!==s&&(e.dispatchEvent(new Event("autosize:resized",{bubbles:!0})),n=s),u!==r.overflow&&!l)){var d=r.textAlign;"hidden"===r.overflow&&(e.style.textAlign="start"===d?"end":"start"),i({restoreTextAlign:d,testForHeightReduction:!0})}}function l(){i({testForHeightReduction:!0,restoreTextAlign:null})}}(e)}),e}).destroy=function(e){return e&&Array.prototype.forEach.call(e.length?e:[e],i),e},c.update=function(e){return e&&Array.prototype.forEach.call(e.length?e:[e],l),e});var u=c;e.s(["default",0,u],711486);var d=e.i(208018),p=e.i(2664),g=e.i(406664),m=e.i(919073),C=e.i(60337);let f=(0,n.forwardRef)(({dataCy:e,style:n,...o},s)=>{let a=(0,g.useCreateInteractiveInput)();return(0,t.jsx)(r.Input,{...o,"data-cy":e,ref:s,clsx:[C.default.input,a.clsx],style:n?{...a.style,...n}:a.style})});f.displayName="Input";let y=(0,n.forwardRef)(({autoSize:e,dataCy:n,style:r,...s},a)=>{let i=(0,g.useCreateInteractiveInput)();return e?(0,t.jsx)(h,{...s,dataCy:n,style:r,ref:a}):(0,t.jsx)(o.TextArea,{...s,"data-cy":n,ref:a,clsx:[C.default.input,i.clsx],style:r?{...i.style,...r}:i.style})});y.displayName="MultiLineInput";let h=(0,n.forwardRef)(({dataCy:e,style:r,...s},a)=>{let{ref:i}=function(){let[e,t]=(0,n.useState)(null);return(0,d.default)(()=>{if(e&&e){let t=new MutationObserver(()=>{u.update(e)});return t.observe(e,{subtree:!0,childList:!0,characterData:!0}),u(e),requestAnimationFrame(()=>{u.update(e)}),()=>{u.destroy(e),t.disconnect()}}},[e]),{ref:t}}(),l=(0,g.useCreateInteractiveInput)(),c=(0,p.useMergeRefs)([a,i],{breadcrumb:"client/rui/Input.tsx"});return(0,t.jsx)(o.TextArea,{...s,ref:c,"data-cy":e,clsx:[C.default.input,C.default.inputAutosize,l.clsx],style:r?{...l.style,...r}:l.style})});h.displayName="MultiLineInputAutosize";let x=(0,n.forwardRef)(({iconLeft:e,iconRight:n,className:o,inputClassName:a,dataCy:i,...l},c)=>{let u=(0,g.useCreateInteractiveInput)();return(0,t.jsxs)(m.ShadesSurface,{clsx:[C.default.decoratedInputRoot,u.clsx,o],style:u.style,elevate:!1,children:[(0,t.jsx)(s.IconProvider,{size:16,children:e}),(0,t.jsx)(r.Input,{...l,"data-cy":i,ref:c,clsx:[C.default.input,C.default.decoratedInputInput,a]}),(0,t.jsx)(s.IconProvider,{size:16,children:n})]})});x.displayName="DecoratedInput";let v=(0,n.forwardRef)(({left:e,right:n,className:o,inputClassName:s,dataCy:a,...i},l)=>{let c=(0,g.useCreateInteractiveInput)();return(0,t.jsxs)(m.ShadesSurface,{clsx:[C.default.decoratedInputRoot,c.clsx,o],style:c.style,elevate:!1,children:[e,(0,t.jsx)(r.Input,{...i,"data-cy":a,ref:l,clsx:[C.default.input,C.default.decoratedInputInput,s]}),n]})});v.displayName="CustomDecoratedInput",e.s(["CustomDecoratedInput",0,v,"DecoratedInput",0,x,"Input",0,f,"MultiLineInput",0,y],528710)},33583,e=>{"use strict";var t=e.i(276385),n=e.i(389959),r=e.i(785240),o=e.i(932200),s=e.i(8047),a=e.i(61732);let i=(0,n.forwardRef)(function({variant:e="small",className:n,color:i,height:l,maxLines:c,multiline:u,dataCy:d,children:p,...g},m){let[{elementType:C,...f},y]=(0,o.useContextProps)(g,m,r.LabelContext);return(0,t.jsx)(s.Text,{variant:e,className:n,color:i,height:l,maxLines:c,multiline:u,dataCy:d,children:(0,t.jsx)(a.SpecializedView.label,{...f,ref:y,children:p})})});e.s(["Label",0,i])},845415,e=>{"use strict";var t=e.i(276385),n=e.i(389959),r=e.i(624071),o=e.i(756841),s=e.i(248033),a=e.i(932200),i=e.i(379778),l=e.i(8047);let c=(0,n.forwardRef)(function({dataCy:e,...n},r){return(0,t.jsx)(o.TextField,{...(0,i.useView)({gap:4}),...n,"data-cy":e,ref:r})}),u=(0,n.forwardRef)(function({variant:e="small",color:n="dimmer",...o},i){let c=(0,a.useSlottedContext)(s.TextContext,"description");return(0,t.jsx)(l.Text,{...(0,r.mergeProps)(o,{variant:e,color:n},c),ref:i})});e.s(["TextField",0,c,"TextFieldDescription",0,u])},137074,e=>{"use strict";var t=e.i(929702),n=e.i(389959);e.s(["useFilter",0,function(e){let r=(0,t.useCollator)({usage:"search",...e}),o=(0,n.useCallback)((e,t)=>0===t.length||(e=e.normalize("NFC"),t=t.normalize("NFC"),0===r.compare(e.slice(0,t.length),t)),[r]),s=(0,n.useCallback)((e,t)=>0===t.length||(e=e.normalize("NFC"),t=t.normalize("NFC"),0===r.compare(e.slice(-t.length),t)),[r]),a=(0,n.useCallback)((e,t)=>{if(0===t.length)return!0;e=e.normalize("NFC");let n=0,o=(t=t.normalize("NFC")).length;for(;n+o<=e.length;n++){let s=e.slice(n,n+o);if(0===r.compare(t,s))return!0}return!1},[r]);return(0,n.useMemo)(()=>({startsWith:o,endsWith:s,contains:a}),[o,s,a])}])}]);

//# debugId=e82d1463-55e4-ea43-b731-d2df83f11738
//# sourceMappingURL=0_72d-_s59w5q.js.map
